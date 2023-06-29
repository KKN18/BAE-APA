package sw.hackathon.baeapa

import android.Manifest
import android.content.ContentValues
import android.content.Intent
import android.content.pm.PackageManager
import android.graphics.Bitmap
import android.net.Uri
import android.os.Bundle
import android.provider.MediaStore
import android.widget.ImageView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import java.io.File

class MainActivity : AppCompatActivity() {

    private val REQUEST_IMAGE_CAPTURE = 1
    private val PERMISSION_REQUEST_CODE = 2
    private lateinit var file: File

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val btnCapture = findViewById<ImageView>(R.id.image_shutter)
        btnCapture.setOnClickListener {
            if (ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA)
                != PackageManager.PERMISSION_GRANTED
            ) {
                ActivityCompat.requestPermissions(
                    this,
                    arrayOf(Manifest.permission.CAMERA),
                    PERMISSION_REQUEST_CODE
                )
            } else {
                launchCamera()
            }
        }
    }

    private fun launchCamera() {
        val intent = Intent(MediaStore.ACTION_IMAGE_CAPTURE)
        val uri = createTemporaryImageFile()
        this.file = File(uri.toString())
        intent.putExtra(MediaStore.EXTRA_OUTPUT, uri)
        startActivityForResult(intent, REQUEST_IMAGE_CAPTURE)

    }

    override fun onRequestPermissionsResult(
        requestCode: Int,
        permissions: Array<out String>,
        grantResults: IntArray
    ) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
        if (requestCode == PERMISSION_REQUEST_CODE) {
            if (grantResults.isNotEmpty() && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                launchCamera()
            } else {
                Toast.makeText(
                    this,
                    "Camera permission denied. Unable to capture photo.",
                    Toast.LENGTH_SHORT
                ).show()
            }
        }
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        if (requestCode == REQUEST_IMAGE_CAPTURE && resultCode == RESULT_OK) {

            val photoFilePath = file.path.replace("content:/", "content://")

            // Start the ResultActivity and pass the photo file path as an intent extra
            val intent = Intent(this, ResultActivity::class.java)
            intent.putExtra("photoFilePath", photoFilePath)
            startActivity(intent)
            //val url = "http://bps.konkuk.ac.kr/siSCANNER/execute_python.php"

//            val url = "http://bps.konkuk.ac.kr/siSCANNER/temp_python.php"
//            val bitmap = BitmapFactory.decodeFile(file.absolutePath)
//            if (bitmap == null){
//                Log.d("결과", "비트맵 NULL")
//            }else{
//                Log.d("결과", bitmap.toString())
//
//            }
//            val inputData = "Hello, PHP!"
//            Log.d("결과", inputData)


            //val bitmap =  BitmapFactory.decodeFile(file.absolutePath, options)
            //println(bitmap)
//            val imageBitmap = data?.extras?.get(MediaStore.EXTRA_OUTPUT) as Bitmap?
//            imageBitmap?.let {
//                val resizedBitmap = resizeBitmap(imageBitmap, -1)
//                saveImageAsPNG(resizedBitmap)
//                saveImageAsPNG(bitmap)
//                Toast.makeText(this, "Image saved as PNG", Toast.LENGTH_SHORT).show()
//            }
        }
    }

    private fun resizeBitmap(bitmap: Bitmap, targetSize: Int): Bitmap {
        val width = bitmap.width
        val height = bitmap.height

//        val scaleWidth = targetSize.toFloat() / width
//        val scaleHeight = targetSize.toFloat() / height

        // Create a matrix for the scaling
        val matrix = android.graphics.Matrix()
//        matrix.postScale(scaleWidth, scaleHeight)

        // Resize the bitmap
        return Bitmap.createBitmap(bitmap, 0, 0, width, height, matrix, true)
    }

    private fun createTemporaryImageFile(): Uri? {
        val contentResolver = applicationContext.contentResolver
        val contentValues = ContentValues().apply {
            put(MediaStore.Images.Media.DISPLAY_NAME, "captured_image.png")
            put(MediaStore.Images.Media.MIME_TYPE, "image/png")
        }

        return contentResolver.insert(
            MediaStore.Images.Media.EXTERNAL_CONTENT_URI,
            contentValues
        )
    }

    private fun saveImageAsPNG(bitmap: Bitmap) {
        val contentResolver = applicationContext.contentResolver
        val contentValues = ContentValues().apply {
            put(MediaStore.Images.Media.DISPLAY_NAME, "captured_image.png")
            put(MediaStore.Images.Media.MIME_TYPE, "image/png")
        }

        val imageUri = contentResolver.insert(
            MediaStore.Images.Media.EXTERNAL_CONTENT_URI,
            contentValues
        )
        imageUri?.let { uri ->
            val outputStream = contentResolver.openOutputStream(uri)
            outputStream?.use { stream ->
                bitmap.compress(Bitmap.CompressFormat.PNG, 100, stream)
                stream.flush()
            }
        }
    }
}
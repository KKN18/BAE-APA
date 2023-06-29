package sw.hackathon.baeapa

import android.graphics.BitmapFactory
import android.net.Uri
import android.os.Bundle
import android.util.Base64
import android.util.Log
import android.widget.ImageView
import android.widget.SeekBar
import androidx.appcompat.app.AppCompatActivity
import androidx.constraintlayout.widget.ConstraintLayout
import androidx.core.content.ContextCompat
import com.android.volley.DefaultRetryPolicy
import com.android.volley.Response
import com.android.volley.toolbox.StringRequest
import com.android.volley.toolbox.Volley
import java.io.ByteArrayOutputStream
import java.lang.Integer.max
import java.lang.Math.min

class ResultActivity : AppCompatActivity() {
    private lateinit var seekBar1: SeekBar
    private lateinit var seekBar2: SeekBar
    private lateinit var seekBar3: SeekBar

    public var progress1 = 50
    public var progress2 = 50
    public var progress3 = 50
    public var num = 1


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_result)

        seekBar1 = findViewById(R.id.seekBar1)
        seekBar2 = findViewById(R.id.seekBar2)
        seekBar3 = findViewById(R.id.seekBar3)

        seekBar1.max = 100
        seekBar2.max = 100
        seekBar3.max = 100

        seekBar1.progress = progress1
        seekBar2.progress = progress2
        seekBar3.progress = progress3


        val photoPath = intent.getStringExtra("photoFilePath")
        val contentResolver = applicationContext.contentResolver
        val uri = Uri.parse(photoPath)

        val inputStream = contentResolver.openInputStream(uri)!!
        val bitmap = BitmapFactory.decodeStream(inputStream)
        val outputStream = ByteArrayOutputStream()
        inputStream.use { input ->
            outputStream.use { output ->
                input.copyTo(output)
            }
        }
        val byteArray = outputStream.toByteArray()
        val base64String: String = Base64.encodeToString(byteArray, Base64.NO_WRAP)

        val imageView = findViewById<ImageView>(R.id.imageView_food)
        imageView.setImageBitmap(bitmap)

        val url = "http://bps.konkuk.ac.kr/siSCANNER/execute_python.php"
        Log.d("결과", base64String)

        // Volley 요청 생성
        val request = object : StringRequest(
            Method.POST, url,
            Response.Listener { response ->
                Log.d("결과1", "굳굳")
                Log.d("결과1", response) // 결과 출력

                if (response != null) {
                    // Conversion successful, use the integer value
                    if (response[0] == '1') {
                        Log.d("결과", "Safe")
                        val firstBox = findViewById<ConstraintLayout>(R.id.first_box)
                        firstBox.setBackgroundColor(ContextCompat.getColor(this, R.color.green))
                    } else if (response[0] == '2') {
                        Log.d("결과", "Normal")
                        val firstBox = findViewById<ConstraintLayout>(R.id.first_box)
                        firstBox.setBackgroundColor(ContextCompat.getColor(this, R.color.orange))
                    } else if (response[0] == '3') {
                        Log.d("결과", "Danger")
                        val firstBox = findViewById<ConstraintLayout>(R.id.first_box)
                        firstBox.setBackgroundColor(ContextCompat.getColor(this, R.color.red))
                    }
                    if (response[1] == '1') {
                        Log.d("결과", "Safe")
                        val secondBox = findViewById<ConstraintLayout>(R.id.second_box)
                        secondBox.setBackgroundColor(ContextCompat.getColor(this, R.color.green))
                    } else if (response[1] == '2') {
                        Log.d("결과", "Normal")
                        val secondBox = findViewById<ConstraintLayout>(R.id.second_box)
                        secondBox.setBackgroundColor(ContextCompat.getColor(this, R.color.orange))
                    } else if (response[1] == '3') {
                        Log.d("결과", "Danger")
                        val secondBox = findViewById<ConstraintLayout>(R.id.second_box)
                        secondBox.setBackgroundColor(ContextCompat.getColor(this, R.color.red))
                    }
                    if (response[2] == '1') {
                        Log.d("결과", "Safe")
                        val thirdBox = findViewById<ConstraintLayout>(R.id.third_box)
                        thirdBox.setBackgroundColor(ContextCompat.getColor(this, R.color.green))
                    } else if (response[2] == '2') {
                        Log.d("결과", "Normal")
                        val thirdBox = findViewById<ConstraintLayout>(R.id.third_box)
                        thirdBox.setBackgroundColor(ContextCompat.getColor(this, R.color.orange))
                    } else if (response[2] == '3') {
                        Log.d("결과", "Danger")
                        val thirdBox = findViewById<ConstraintLayout>(R.id.third_box)
                        thirdBox.setBackgroundColor(ContextCompat.getColor(this, R.color.red))
                    }

                    updateBarColors(response)
                    

                    seekBar1.isEnabled = false
                    seekBar2.isEnabled = false
                    seekBar3.isEnabled = false

                } else {
                    // Conversion failed, handle the error case
                    Log.e("결과", "Failed to convert response to an integer.")
                }
            },
            Response.ErrorListener { error ->
                Log.e("결과", error.toString())
            }) {
            override fun getParams(): MutableMap<String, String> {
                val params = HashMap<String, String>()
                params["image"] = base64String
                return params
            }
        }.apply {
            retryPolicy = DefaultRetryPolicy(
                30000,
                DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                DefaultRetryPolicy.DEFAULT_BACKOFF_MULT
            )
        }
        Volley.newRequestQueue(this).add(request)
    }

    private fun updateBarColors(str: String) {
        num += 1
        val level1: Int = (str[0] - '0').toInt()
        val level2: Int = (str[1] - '0').toInt()
        val level3: Int = (str[2] - '0').toInt()

        updateBarColor(seekBar1, level1, progress1, 1)
        updateBarColor(seekBar2, level2, progress2, 2)
        updateBarColor(seekBar3, level3, progress3, 3)
    }

    private fun updateBarColor(seekBar: SeekBar, level: Int, curProgress: Int, flag: Int) {
        val base = when (level) {
            1 -> 0
            2 -> 50
            3 -> 100
            else -> 50
        }
        Log.d("DDDcurProgress", "$curProgress")
        Log.d("DDDbase", "$base")
        Log.d("DDDnum", "$num")

        val change: Int = ((base - curProgress).toDouble() / num).toInt()
        var value = curProgress + change
        value = max(0, min(100, value))
        Log.d("DDDvalue", "$value")

        if (flag == 1) progress1 = value
        if (flag == 2) progress2 = value
        if (flag == 3) progress3 = value
        seekBar.progress = value
    }
}
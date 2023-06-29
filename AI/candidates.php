<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // $input = $_POST['input']; // 안드로이드 앱에서 전달한 입력 데이터
    $base64Image = $_POST['image'];

    // base64 이미지 디코딩
    $imageData = base64_decode($base64Image);

    // 이미지 저장
    $outputPath = 'inputimg.jpg';
    $check = 'checkpoint.pth'
    file_put_contents($outputPath, $imageData);

    // Python 코드 실행
    $output = shell_exec('python3.6 candidates.py ' . escapeshellarg($check + " "+$outputPath));
    // 위 코드에서 'execute.py'를 실행하고, 이미지 파일 경로를 파라미터로 전달합니다.

    // 결과 반환
    echo $output;
}
?>

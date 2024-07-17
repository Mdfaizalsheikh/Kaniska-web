<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enhanced 3D Website with A-Frame</title>
    <script src="https://aframe.io/releases/1.2.0/aframe.min.js"></script>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    

    <a-scene embedded>
        <a-sky color="#000000"></a-sky>
        <a-entity particle-system="preset: stars; particleCount: 1000 "></a-entity>
        
        <a-sphere position="0 1.25 -5" radius="1.25" color="#00f" segments-height="18" segments-width="36">
            <a-animation attribute="rotation" dur="20000" fill="forwards" to="0 360 0" repeat="indefinite"></a-animation>
        </a-sphere>
        
        <a-sphere position="3 0.5 -5" radius="0.5" color="#aaa">
            
            <a-animation attribute="rotation" dur="20000" fill="forwards" to="0 -360 0" repeat="indefinite"></a-animation>
            
        </a-sphere>
        
        <a-sphere position= "0 3 -10" radius="1" color="#FF4500">
            <a-animation attribute="rotation" dur="20000" fill="forwards" to="0 360 0" repeat="indefinite"></a-animation>
        </a-sphere>
      
        

        <a-entity camera look-controls>
            <a-cursor></a-cursor>
        </a-entity>
        
    </a-scene>

    <script src="script.js"></script>
</body>
</html>

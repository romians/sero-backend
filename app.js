document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const fileInput = document.getElementById('imageInput');
    const formData = new FormData();
    formData.append('image', fileInput.files[0]);

    // 이미지 파일을 읽어서 미리보기로 보여주기
    if (fileInput.files && fileInput.files[0]) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const uploadedImage = document.getElementById('uploadedImage');
            uploadedImage.src = e.target.result;
            uploadedImage.style.display = 'block';
        };
        reader.readAsDataURL(fileInput.files[0]);
    }

    // 서버로 이미지 파일을 전송하고 응답 받기
    fetch('/upload', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('responseArea').textContent = JSON.stringify(data, null, 2);
    })
    .catch(error => console.error('Error:', error));
});

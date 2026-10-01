document.addEventListener('DOMContentLoaded', function () {
  document.querySelector('#btn_translate').addEventListener('click', function () {
    const code = document.querySelector('#language_code').value;
    fetch('https://hellosalut.stefanbohacek.com/?lang=' + code)
      .then(response => response.json())
      .then(data => {
        document.querySelector('#hello').textContent = data.hello;
      });
  });
});

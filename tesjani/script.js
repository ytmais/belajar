document.getElementById('form-kontak').addEventListener('submit', function (e) {
    e.preventDefault();

    var nama = this.nama.value.trim();
    var email = this.email.value.trim();
    var pesan = this.pesan.value.trim();
    var status = document.getElementById('status-pesan');

    if (nama === '' || email === '' || pesan === '') {
        status.textContent = 'Mohon lengkapi semua kolom.';
        status.className = 'status gagal';
        status.style.display = 'block';
        return;
    }

    status.textContent = 'Pesan Anda berhasil dikirim. Terima kasih, ' + nama + '!';
    status.className = 'status sukses';
    status.style.display = 'block';

    this.reset();
    setTimeout(function () {
        status.style.display = 'none';
    }, 5000);
});
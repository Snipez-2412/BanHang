document.addEventListener("DOMContentLoaded", function() {
    // Lấy các phần tử cần thiết
    const decreaseButton = document.getElementById("decrease");
    const increaseButton = document.getElementById("increase");
    const quantityInput = document.getElementById("quantity");

    // Khi nhấn nút giảm (decrease)
    decreaseButton.addEventListener("click", function() {
        let currentQuantity = parseInt(quantityInput.value); // Lấy số lượng hiện tại
        if (currentQuantity > 1) {
            quantityInput.value = currentQuantity - 1; // Giảm số lượng
        }
    });

    // Khi nhấn nút tăng (increase)
    increaseButton.addEventListener("click", function() {
        let currentQuantity = parseInt(quantityInput.value); // Lấy số lượng hiện tại
        quantityInput.value = currentQuantity + 1; // Tăng số lượng
    });

    // Khi thay đổi trực tiếp trong ô nhập số lượng (tự động điều chỉnh nếu nhập không hợp lệ)
    quantityInput.addEventListener("input", function() {
        let currentQuantity = parseInt(quantityInput.value);
        if (isNaN(currentQuantity) || currentQuantity < 1) {
            quantityInput.value = 1; // Nếu nhập không hợp lệ, đặt lại về 1
        }
    });
});

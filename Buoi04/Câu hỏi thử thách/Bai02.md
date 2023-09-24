Có một số trường hợp ta chỉ có thể lặp bằng cấu trúc while mà không thể lặp bằng cấu trúc for. Một ví dụ là khi ta không biết trước số lần lặp.

for (i = 0; i < n; i++) { // do something }

Trong đoạn code trên, biến i được khởi tạo với giá trị 0 và tăng lên 1 sau mỗi lần lặp. Vòng lặp sẽ dừng khi i bằng n. Tuy nhiên, nếu ta không biết trước giá trị của n thì ta không thể sử dụng vòng lặp for.

Một ví dụ khác là khi ta muốn lặp lại một khối code cho đến khi một điều kiện nào đó được đáp ứng.

while (true) { // do something if (condition) { break; } }

Trong đoạn code trên, vòng lặp while sẽ tiếp tục chạy cho đến khi điều kiện condition được đáp ứng. Nếu ta sử dụng vòng lặp for trong trường hợp này, thì vòng lặp sẽ dừng sau một số lần lặp nhất định, ngay cả khi điều kiện condition chưa được đáp ứng.
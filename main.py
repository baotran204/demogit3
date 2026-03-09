def tinh_tong(a, b):
    return a + b


def main():
    print("Chương trình tính tổng hai số")

    a = int(input("Nhập số thứ nhất: "))
    b = int(input("Nhập số thứ hai: "))

    ket_qua = tinh_tong(a, b)

    print("Tổng của", a, "và", b, "là:", ket_qua)


if __name__ == "__main__":
    main()
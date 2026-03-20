day = input("今天是周几？（请输入1-7）:")
match day:
	case "1":
		print("周一")
	case "2":
		print("周二")
	case "3":
		print("周三")
	case "4":
		print("周四")
	case "5":
		print("周五")
	case "6" | "7":
		print("周末")
	case "8" | "9" if day == "9":
		print("测试case if条件")
	case _:
		print("错误！")

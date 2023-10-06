if __name__ == '__main__':
    num = int(input())
    size_list = list(map(int, input().split()))
    customer_num = int(input())
    
    total_earned = 0

    for i in range(customer_num):
        size_pay = list(map(int, input().split()))
        if size_pay[0] in size_list:
            size_list.remove(size_pay[0])
            total_earned += size_pay[1]
        else:
            pass
    
    print(total_earned)
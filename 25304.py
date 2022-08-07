## 영수증 문제
# 리스트에서 
def multiply(value):
    # 리스트안의 
    return value[0] * value[1]

def method(X, receipt_list):
    calculate_receipt = sum([multiply(value) for value in receipt_list])

    if X == calculate_receipt:
        answer = "Yes"
    else:
        answer = "No"

    return answer

if __name__ == "__main__":
    # 
    X = int(input())

    n = int(input())
    
    receipt_list = []

    for i in range(n):
        
        price, num = map(int, input().split())
        receipt_list.append((price, num))
    
    print(method(X, receipt_list))


## 영수증 문제
# 리스트에서 
def multiply(value):
    # 리스트안의 소괄호 값 곱하기
    return value[0] * value[1]

def method(X, receipt_list):
    # for문을 python 방식으로 진행
    calculate_receipt = sum([multiply(value) for value in receipt_list])
    # 정답을 return 
    if X == calculate_receipt:
        answer = "Yes"
    else:
        answer = "No"

    return answer

if __name__ == "__main__":
    # 영수증 총액 받기
    X = int(input())
    # 영수증 구매한 iterm 개수
    n = int(input())
    
    receipt_list = []

    for i in range(n):
        # 가격과 몇개 샀는지 받기
        price, num = map(int, input().split())
        receipt_list.append((price, num))
    
    print(method(X, receipt_list))


#기본 금액 : balance
#기본 금액에 돈을 넣어주세요
#while문을 이용해서 입금, 출금, 영수증 보기,종료하는 기능이 버튼을 누리기 전까지 계속해서 노출되도록 만들어주세요
#종류를 누르면 서비스를 종류한다는 메시지를 출력하고 현재 잔액을 보여주세요.
#출금 요청 금액으 받는 변수 : withdraw_amout
#출금한 금액을 balance 변수에 뺀 결과가 들어가도록 코드를 작성해 주세요.
#영주증에 다음 순서를 값이 들어가도록 코드를 만들어 주세요. -> "출금", 출금 요청액, 총액 순으로 데이터 넣어주세요.
#가지고 있는 금액보다 출금을 원하는 금액이 클때 가지고 있는 금액만 출금 되도록 작성해 주세요.
#단, 영수증에 내역을 변경되지 않아야 하며 입금 또는 출금이 진행될대마다 이력이 기록됩니다.
#영수증 변수는 : receipts
# 입력 검증 및 에러 처리추가, 잘못된 입력 값(숫자가 아닌값, 음수 값 등)
# 유효하지 않는 메뉴 선택 시 경고 메세지 또는 사용방법 재안내를 해주세요.

receipts = [] 
balnce = 3000

while True:
    print()
    num = input("사용하실 기능을 선택해주세요 (1: 입금, 2:출금, 3:영수증 보기, 4:종료)")
    if num == '4':
        break
    if num == '1':
        deposit_amount = input('입금하실 금액을 입력해 주세요. : ')
        if deposit_amount.isdigit() and int(deposit_amount) > 0: #1000 -> True, 천원 -> False
            balnce = balnce + int(deposit_amount)
            receipts.append(("입금", deposit_amount, balnce))
            print(f'입금하신 금액은 {deposit_amount}원이고, 현재 잔액은 {balnce}원 입니다.')
        else:
            print("입금한 금액을 숫자 형태와 음수가 아닌값을 입력해주세요.")
            
    if num == '2':
        withdraw_amout = int(input("출금 하실 금액을 입력해 주세요. : "))
        withdraw_amout = min(balnce, withdraw_amout)
        balnce -= withdraw_amout
        receipts.append(("출금", withdraw_amout, balnce))
        print(f'출금하신 금액은 {withdraw_amout}원이고, 현재 잔액은 {balnce}원 입니다.')

    if num == '3':
        if receipts:
            print("===영수중===")
            for i in receipts:
                print(f'{i[0]}: {i[1]}원, 잔액:{i[2]}원 입니다')
        else:
            print("영수증 내력이 없습니다")


print(f'서비스를 종류합니다. 현재 남은 금액은{balnce}입니다.')
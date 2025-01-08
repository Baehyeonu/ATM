#기본 금액 : balance
#기본 금액에 돈을 넣어주세요
#while문을 이용해서 입금, 출금, 영수증 보기,종료하는 기능이 버튼을 누리기 전까지 계속해서 노출되도록 만들어주세요
#종류를 누르면 서비스를 종류한다는 메시지를 출력하고 현재 잔액을 보여주세요.
#입금한 금액으 받는 변수 : deporsit_amout
#입금된 금액을 balance 변수에 추가되도록 코드를 작성해 주세요.
#영주증에 다음 순서를 값이 들어가도록 코드를 만들어 주세요. -> "입금", 입금 요청액, 총액 순으로 데이터 넣어주세요.
#단, 영수증에 내역을 변경되지 않아야 하며 입금 또는 출금이 진행될대마다 이력이 기록됩니다.
#영수증 변수는 : receipts

receipts = [()] 
balnce = 3000

while True:
    num = input("사용하실 기능을 선택해주세요 (1: 입금, 2:출금, 3:영수증 보기, 4:종료)")
    if num == '4':
        break
    if num == '1':
        deporsit_amout = int(input('입금하실 금액을 입력해 주세요. :'))
        balnce = balnce + deporsit_amout
        receipts.append(("입금", deporsit_amout, balnce))
        print(f'입금하신 금액은 {deporsit_amout}원이고, 현재 잔액은 {balnce}원 입니다.')
print(f'서비스를 종류합니다. 현재 남은 금액은{balnce}입니다.')
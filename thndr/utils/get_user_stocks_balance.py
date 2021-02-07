def get_user_stocks_balance(user_id, stock_uuid):
    from thndr.models import Transaction
    balance = 0
    txs = Transaction.objects.filter(user__pk=user_id, stock__stock_uuid=stock_uuid)
    for tx in txs:
        if tx.stock:
            if tx.deposit:
                balance = balance + tx.amount
            elif tx.withdraw:
                balance = balance - tx.amount
    return balance

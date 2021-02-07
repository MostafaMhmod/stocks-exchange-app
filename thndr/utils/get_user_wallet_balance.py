def get_user_wallet_balance(user_id):
    from thndr.models import Transaction
    balance = 0
    txs = Transaction.objects.filter(user__pk=user_id)
    for tx in txs:
        if not tx.stock:
            if tx.deposit:
                balance = balance + tx.amount
            elif tx.withdraw:
                balance = balance - tx.amount
    return balance

- Here we can 2 different types of exchanges
- 1. Direct Exchange
- 2. Topic Exchange

1. Direct exchange
   Here we have to use a routing key which is used to check to which queue the message should be forwarded to by the exchange

2. Topic exchange
   Here also, we use a routing key, but the difference is this is more flexible than the direct exchnage because we can use wildcards to match the routing key
   _ -> Will match only one word ( _.europe.purchase, user.europe._, _.america.\*) # -> Will match any number of words ( #.purchase, user.#)

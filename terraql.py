from string import Template


class terraQL(object):
    
    def __init__(self, account):
        self.account = str(account)

    
    #returns ALL AVAILABLE mirror assets + statistics
    def mirror_assets(url='https://graph.mirror.finance/graphql'):
        query = '''{
              assets {
                symbol
                name
                prices {
                  price
                  oraclePrice
                }
                pair
                lpToken
                statistic {
                  liquidity
                  volume
                  apr
                  apy
                }
              }
            }'''
                
        return query
    
    #returns account transactions
    def account_transactions(self, offset,
                             url='https://graph.mirror.finance/graphql'):
        query =  '''{
              txs(account: {0}, offset: 0, limit: {1}) {
                createdAt
                id
                height
                txHash
                address
                type
                data
                token
                datetime
                fee
                tags
                memo
                __typename
              }
            }'''.replace('{0}', self.account).replace('{1}', str(offset))
              
        return query
    
    #returns terra_wallet coins (does not include mAssets)
    def terra_wallet(self, url='https://mantle.terra.dev/'):
        query =  '''{
             BankBalancesAddress(Address: {0}){
                Height
                Result {
                  Amount
                  Denom
                }
            }
            '''.replace('{0}', self.account)
              
        return query
    
    #returns major overall terra network stats
    def terra_network(url='https://graph.mirror.finance/graphql'):
        query =  '''{
              statistic(network:”TERRA”) {
                assetMarketCap
                totalValueLocked
                collateralRatio
                mirCirculatingSupply
                govAPR
                govAPY
                latest24h {
                  transactions
                  volume
                  feeVolume
                  mirVolume
                  __typename
                }
                __typename
              }
            }'''

              
        return query
    
    #this gets holdings from mirror my page
    def maccount_holding_info(self, mtoken_address,
                          url='https://mantle.terra.dev/'):        
        query =  Template('''{
                WasmContractsContractAddressStore(
                ContractAddress: $mtokenaddress
                QueryMsg: $msg
              ) {
                Height
                Result
                __typename
              }
            }
            ''')
            
        message = '''"{\"balance\":{\"address\":\"{0}\"}}"'''.replace(
                '{0}',self.account) 
        
        query = query.substitute(msg=message, mtokenaddress=mtoken_address)
              
        return query
              
    
    #returns my stakes, bond amounts, and pending rewards (rewards are 0?)
    #the bond amount is number of LP tokens staked (does not include unstaked)
    def maccount_stake_info(self, url='https://mantle.terra.dev/'):
        query =  Template("""query {
            WasmContractsContractAddressStore(
            ContractAddress: "terra17f7zu97865jmknk7p2glqvxzhduk78772ezac5"
            QueryMsg: $msg
          ) {
            Height
            Result
            __typename
          }
        }
        """)

        message = '''"{\\"reward_info\\":{\\"staker\\":\\"{0}\\"}}"'''.replace(
                '{0}',self.account)     
        query = query.substitute(msg=message)
              
        return query
    
    #token pair address comes from mirror assets call
    # gets pool statistics, total amount lp tokens, Token Amount, UST Amount
    def mirror_pool_info(self, token_pair, url='https://mantle.terra.dev/'):
        query =  Template("""query {
            WasmContractsContractAddressStore(
            ContractAddress: $tp
            QueryMsg: $msg
          ) {
            Height
            Result
            __typename
          }
        }
        """)
        
        message = '''"{\"pool\":{}}"'''
        query = query.substitute(msg=message)
        query = query.substitute(tp=token_pair)
              
        return query
    
    #returns staking info for mirror token contracts like total bond amount
    def mirror_stake_info(self, mtoken_address, url='https://mantle.terra.dev/'):
        query =  Template("""query {
            WasmContractsContractAddressStore(
            ContractAddress: "terra17f7zu97865jmknk7p2glqvxzhduk78772ezac5"
            QueryMsg: $msg
          ) {
            Height
            Result
            __typename
          }
        }
        """)

        message = '''"{\"pool_info\":{\"asset_token\":\"{0}\"}}"'''.replace(
                '{0}', mtoken_address)     
        query = query.substitute(msg=message)
              
        return query
    
    #token pair address comes from mirror assets call 
    #returns staking info for mirror token contracts like total bond amount
    def maccount_unstaked_lp(self, lptoken, url='https://mantle.terra.dev/'):
        query =  Template("""query {
            WasmContractsContractAddressStore(
            ContractAddress: $lpt
            QueryMsg: $msg
          ) {
            Height
            Result
            __typename
          }
        }
        """)

        message = '''"{\"balance\":{\"address\":\"{0}\"}}"'''.replace(
                '{0}', self.account)     
        query = query.substitute(msg=message)
        query = query.substitute(lpt=lptoken)
              
        return query
    
    def mint_configs(self, mtoken_address, url='https://mantle.terra.dev/'):
        query =  Template("""query {
            WasmContractsContractAddressStore(
            ContractAddress: "terra1wfz7h3aqf4cjmjcvc6s8lxdhh7k30nkczyf0mj"
            QueryMsg: $msg
          ) {
            Height
            Result
            __typename
          }
        }
        """)

        message = '''"{\"asset_config\":{\"asset_token\":\"{0}\"}}"'''.replace(
                '{0}', mtoken_address)     
        query = query.substitute(msg=message)
              
        return query
    









import time
from web3 import Web3

# Адрес узла (RPC) сети Sonic. Это "входная дверь" в блокчейн.
SONIC_RPC_URL = "https://rpc.soniclabs.com" 

def check_sonic_network():
    # Создаем подключение
    w3 = Web3(Web3.HTTPProvider(SONIC_RPC_URL))
    
    print("🔄 Попытка подключения к сети Sonic...")
    
    if w3.is_connected():
        start_time = time.time()
        # Получаем номер последнего блока в сети
        block_number = w3.eth.block_number
        # Считаем задержку в миллисекундах
        latency = (time.time() - start_time) * 1000
        
        print("-" * 30)
        print(f"✅ Статус: ПОДКЛЮЧЕНО")
        print(f"📦 Последний блок в сети: {block_number}")
        print(f"⚡ Скорость отклика: {latency:.2f} ms")
        print("-" * 30)
        print("💡 Совет: Сделай скриншот этого окна для отчета!")
    else:
        print("❌ Ошибка: Не удалось подключиться. Проверь интернет.")

if __name__ == "__main__":
    check_sonic_network()

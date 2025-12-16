# 這個function的主要目的是從另一家公司(zht)的圖資系統(tms)把圖資相關的table都import進來
# 此外還要處理以下問題：
# 1. tms的資料是兩個欄位(UFID, REGION_CODE)合起來才unique，但我們想把他合併成一個欄位
# 2. 為了效能考量，我們必須把每個table可能高達上百萬筆的資料，批次寫入

# 輸入參數mappings的解說如下
# mappings的主要作用是source DB跟target DB的table name及field name的對應關係
# 例如mappings如下時：
# {
#   "Pole": {
#     "table": "_pole",
#     "fields": ["ufid", "x", "y"]
#     "prepend_regions": {
#       "ufid": {
#         "precision": 8
#       }
#     }
#   }
# }
#
# 假設來源table(_pole)資料如下：
# ufid, region_code, x,   y
# 1,  12,     23.659, 120.174
# 2,  3,      22.874, 120.537

# 產出的目標table(Pole)資料應為:
# ufid,    x,    y
# 01200000001, 23.659, 120.174
# 00300000002, 22.874, 120.537


MAX_RECORD_PER_ROUND = 10000


def import_data_from_zht_tms_backup(mappings, dst_conn, dst_cursor):
    src_conn = psycopg2.connect(
        host='192.168.1.236', database='iot', user='thingnario', password='thingnario')
    src_cursor = src_conn.cursor()

    for dst_table_name, mapping in mappings.items():
        src_table_name = mapping["table"]
        print('import table {} start'.format(src_table_name))
        fields = mapping["fields"]
        field_count = len(fields)
        prepending_config = mapping["prepend_regions"]

        src_cursor.execute('SELECT COUNT(*) FROM public.{}'.format(src_table_name))
        total_records = src_cursor.fetchone()[0]
        print('total_records: ', total_records)

        counts = total_records
        while counts > 0:
            cmd = """
                SELECT {}, _region_code FROM public.{} order by _id asc limit {} offset {}
                """.format(
                    ','.join(fields),
                    src_table_name,
                    MAX_RECORD_PER_ROUND,
                    total_records - counts)
            src_cursor.execute(cmd)
            records = src_cursor.fetchall()
            counts -= MAX_RECORD_PER_ROUND

            query = """
                REPLACE INTO thingnario_tms.{}({}) VALUES({})
                """.format(
                    dst_table_name,
                    ','.join(fields),
                    ','.join(['%s'] * field_count))

            bulk_data = []
            for record in records:
                region_code = record[-1]
                processed = map(
                    lambda index, value:
                        prepend_region_code(value, region_code)
                        if fields[index] in prepending_config else value,
                    enumerate(record[:-1]))
                bulk_data.append(tuple(processed))

            try:
                dst_cursor.executemany(query, bulk_data)
                dst_conn.commit()
            except Exception as e:
                print(e)


# 1. src_conn, src_cursor 抽到外面為參數
# 2. 將 batch_read, batch_insert, process_data 的 function 抽出


DB_HOST='192.168.1.236'
DB_NAME = 'iot'
DB_USER = 'thingnario'
DB_PASS = 'thingnario'

# Intialize session
src_conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
src_cursor = src_conn.cursor()


def import_data_from_backup(db_cursor, db_name, mapping):
    """
    Handle backup a source table to new table
    """
    pass

def get_amount(db_cursor, db_name) -> int:
    """
    Get amount of data
    """
    pass

def batch_get_data(db_name, fields, limit, offset):
    """
    Batch get data by page
    """

def bulk_insert(db_name, data):
    """
    Bulk insert data
    """ 

def main():
    
    # Intialize session
    src_conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
    src_cursor = src_conn.cursor()

    # Get all mappings
    for dst_table_name, mapping in mappings.items():
        src_table_name = mapping["table"]
        # 

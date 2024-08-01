import psycopg2

hostname = 'localhost'
database = '401kfees'
username = 'postgres'
pwd = 'psqltesting'
port_id = 5432

try:
    conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id)
    cur = conn.cursor()
    # delete_table = '''DROP TABLE fee_data'''
    create_script = ''' CREATE TABLE fee_data (
                            company_name            varchar(50),
                            record_keeper           varchar(50),
                            participants            varchar(50),
                            assets                  int,
                            total_inv               float,
                            rev_share               float,
                            net_inv                 float,
                            rk_sponsor_fee          int,
                            rk_ppt_fee              float,
                            ppt_service_fees        int,
                            trustee_custodial_fee   int,
                            participant_advice      int)'''
    # cur.execute(delete_table)
    cur.execute(create_script)
    conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
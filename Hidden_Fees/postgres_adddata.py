from turtle import update
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
    
    # FOR ADDING A RECORD
    # insert_script = 'INSERT INTO fee_data (company_name, record_keeper, participants, assets, total_inv, rev_share, net_inv, rk_sponsor_fee, rk_ppt_fee, ppt_service_fees, trustee_custodial_fee, participant_advice) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    # insert_value = ('yes', 'yes', 'yes', 1, 0.1, 0.1, 0.1, 3, 0.1, 3, 4, 4)
    # cur.execute(insert_script, insert_value)
    
    # FOR DELETING A RECORD
    # delete_script = 'DELETE FROM fee_data WHERE company_name = %s'
    # delete_record = ('yes',)
    # cur.execute(delete_script, delete_record)
    
    #FOR UPDATING A COLUNMN NAME
    # update_script = "ALTER TABLE fee_data RENAME COLUMN company_name TO company_name"
    # cur.execute(update_script)
    # conn.commit()
    

# Commit the changes
    conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
        

#IF YOU WANT TO EXPORT THE TABLE TO A CSV
# import csv

# cursor = connection.cursor()
# cursor.execute("SELECT * FROM fee_data;")

# # Fetch column names
# column_names = [desc[0] for desc in cursor.description]

# # Write to CSV file
# with open('output.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(column_names)  # Write header
#     writer.writerows(cursor)      # Write data

# cursor.close()
# connection.close()
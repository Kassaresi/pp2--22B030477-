sql_create_table = """
CREATE TABLE IF NOT EXISTS  phonebook (
    human_id SERIAL PRIMARY KEY,
    contact text NOT NULL,
    phone_num text NOT NULL
)
"""

sql_select_filter_name = "SELECT contact FROM phonebook"
sql_select_filter_id = "SELECT human_id FROM phonebook"
sql_select_filter_phone = "SELECT phone_num FROM phonebook"
sql_select_filter_name_id = "SELECT human_id, contact FROM phonebook"
sql_select_filter_name_phone = "SELECT contact, phone_num FROM phonebook"
sql_select_filter_id_phone = "SELECT human_id, phone_num FROM phonebook"
sql_select_filter_id_phone_name = "SELECT human_id, contact, phone_num FROM phonebook"


sql_upload_from_csv = """COPY phonebook(contact, phone_num)
FROM %s
DELIMITER ','
CSV HEADER;"""

sql_entering_from_console = """
INSERT INTO phonebook(contact, phone_num) VALUES (%s, %s)
"""

sql_change_name_by_id = "UPDATE phonebook SET contact = %s WHERE human_id = %s"

sql_change_phone_by_id =  "UPDATE phonebook SET phone_num = %s WHERE human_id = %s"

sql_change_name_by_name = "UPDATE phonebook SET contact = %s WHERE contact = %s"
sql_change_name_by_phone = "UPDATE phonebook SET contact = %s WHERE phone_num = %s"


sql_change_phone_by_name =  "UPDATE phonebook SET phone_num = %s WHERE contact = %s"

sql_check_exist_by_name = "SELECT COUNT(*) FROM phonebook WHERE contact = %s"
sql_check_exist_by_phone = "SELECT COUNT(*) FROM phonebook WHERE phone_num = %s"

sql_select_by_name = "SELECT * FROM phonebook WHERE contact = %s"
sql_select_by_phone = "SELECT * FROM phonebook WHERE phone_num = %s"


sql_delete_by_name = "DELETE FROM phonebook WHERE contact = %s"
sql_delete_by_id = "DELETE FROM phonebook WHERE human_id = %s"
sql_delete_by_phone = "DELETE FROM phonebook WHERE phone_num = %s"
sql_clear_all = "TRUNCATE TABLE phonebook"

sql_search_by_pattern = "SELECT * FROM phonebook WHERE contact LIKE %s or phone_num LIKE %s LIMIT 10 OFFSET %s"
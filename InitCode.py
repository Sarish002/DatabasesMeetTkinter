import sqlite3

Time  = sqlite3.connect('Time.db')
Timmy = Time.cursor()
Timmy.execute('CREATE TABLE info (name text, dob text, gender text, fatnam text, motnam text, phone integer, examavg1 integer, examavg2 integer, code text)')
Time.commit()
Time.close()
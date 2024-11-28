from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS attendance
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         date DATE NOT NULL,
         status TEXT NOT NULL,
         notes TEXT)
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    
    # Get all attendance records ordered by date
    c.execute('SELECT * FROM attendance ORDER BY date DESC')
    attendance_records = c.fetchall()
    
    conn.close()
    return render_template('index.html', attendance_records=attendance_records)

@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    date = request.form.get('date')
    status = request.form.get('status')
    notes = request.form.get('notes')
    
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    
    # Check if attendance already exists for this date
    c.execute('SELECT id FROM attendance WHERE date = ?', (date,))
    existing = c.fetchone()
    
    if existing:
        c.execute('UPDATE attendance SET status = ?, notes = ? WHERE date = ?',
                 (status, notes, date))
    else:
        c.execute('INSERT INTO attendance (date, status, notes) VALUES (?, ?, ?)',
                 (date, status, notes))
    
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
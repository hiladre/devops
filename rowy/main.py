import os
import psycopg2

def main():
    job_id = os.getenv("JOB_ID")
    if not job_id:
        raise ValueError("JOB_ID environment variable not set")

    conn = psycopg2.connect(host="db", database="mydb", user="user", password="password")
    cur = conn.cursor()
    cur.execute("INSERT INTO jobs (id) VALUES (%s)", (job_id,))
    conn.commit()
    cur.close()
    conn.close()
    print(f"Inserted job ID: {job_id}")

if __name__ == "__main__":
    main()

# MySQL advanced

```
josephgreen@JosephGreen-Mugabi:~$ echo "SELECT * FROM users" | mysql -uroot -p holberton
Enter password: 
id      email   name
1       bob@dylan.com   Bob
2       sylvie@dylan.com        Sylvie
josephgreen@JosephGreen-Mugabi:~$ 

mysql> show databases;
+-----------------------+
| Database              |
+-----------------------+
| information_schema    |
| data_stor_eng_dev_db  |
| data_stor_eng_test_db |
| hbtn_0d_tvshows       |
| holberton             |
| mysql                 |
| performance_schema    |
| sys                   |
+-----------------------+
8 rows in set (0.02 sec)

mysql> use holberton;

Database changed
mysql> SELECT * FROM users
    -> ;
+----+------------------+--------+
| id | email            | name   |
+----+------------------+--------+
|  1 | bob@dylan.com    | Bob    |
|  2 | sylvie@dylan.com | Sylvie |
+----+------------------+--------+
2 rows in set (0.00 sec)
```
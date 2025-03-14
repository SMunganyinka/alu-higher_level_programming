-- This script lists all privileges of MySQL users 'user_0d_1' and 'user_0d_2' on localhost.

SELECT user, host, Db, 
       Select_priv, Insert_priv, Update_priv, Delete_priv, Create_priv, Drop_priv, 
       Reload_priv, Shutdown_priv, Process_priv, File_priv, Grant_priv, References_priv, 
       Index_priv, Alter_priv, Show_db_priv, Super_priv, Create_tmp_table_priv, 
       Lock_tables_priv, Execute_priv, Repl_slave_priv, Repl_client_priv, 
       Create_view_priv, Show_view_priv, Create_routine_priv, Alter_routine_priv, 
       Create_user_priv, Event_priv, Trigger_priv 
FROM mysql.db 
WHERE user IN ('user_0d_1', 'user_0d_2') AND host = 'localhost';

SELECT user, host, 
       Select_priv, Insert_priv, Update_priv, Delete_priv, Create_priv, Drop_priv, 
       Reload_priv, Shutdown_priv, Process_priv, File_priv, Grant_priv, References_priv, 
       Index_priv, Alter_priv, Show_db_priv, Super_priv, Create_tmp_table_priv, 
       Lock_tables_priv, Execute_priv, Repl_slave_priv, Repl_client_priv, 
       Create_view_priv, Show_view_priv, Create_routine_priv, Alter_routine_priv, 
       Create_user_priv, Event_priv, Trigger_priv 
FROM mysql.user 
WHERE user IN ('user_0d_1', 'user_0d_2') AND host = 'localhost';

-- Alternative method using SHOW GRANTS
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';

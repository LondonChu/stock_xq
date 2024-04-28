import pymssql, os, sys
from Common.globals import *


### 取得 MSSQL 連線資訊
def GetDBConnect():
    ### local mssql
    os.environ['MSSQL_HOST'] = 'localhost'
    os.environ['MSSQL_PORT'] = str(1433)
    # os.environ['MSSQL_USER'] = 'sa'
    # os.environ['MSSQL_PASSWORD'] = '@Dvantech9667'
    os.environ['MSSQL_DATABASE'] = 'stock'

    print("MSSQL_HOST : ", os.environ['MSSQL_HOST'])
    print("MSSQL_PORT : ", os.environ['MSSQL_PORT'])
    # print("MSSQL_USER : ", os.environ['MSSQL_USER'])
    # print("MSSQL_PASSWORD : ", os.environ['MSSQL_PASSWORD'])
    print("MSSQL_DATABASE : ", os.environ['MSSQL_DATABASE'])

    try:
        conn = pymssql.connect(
            host = os.environ['MSSQL_HOST'],
            port = os.environ['MSSQL_PORT'],
            # user = os.environ['MSSQL_USER'],
            # password = os.environ['MSSQL_PASSWORD'],
            database = os.environ['MSSQL_DATABASE']
        )
        return conn
    except pymssql.Error as e:
        LOGGER.exception("DB Connect Error : %s", str(e))
    return


### 取得 SQL 查詢結果
def sql_SelectCmd(sqlcmd):
    try:
        conn = GetDBConnect()
        cursor = conn.cursor(as_dict=True)
        cursor.execute(sqlcmd)
        result = cursor.fetchall()
        return result
    except pymssql.Error as e:
        LOGGER.exception("SQL CMD Error : %s", sqlcmd)
        LOGGER.exception("sql_SelectCmd Function Error : %s", e)
        return str(e)
    finally:
        if conn != None:
            cursor.close()
            conn.close()
    return


### 取得 SQL 查詢結果資料筆數
def sql_SelectRowCount(sqlcmd):
    try:
        conn = GetDBConnect()
        cursor = conn.cursor(as_dict=True)
        cursor.execute(sqlcmd)
        rows = cursor.fetchall()
        result = cursor.rowcount
        return result
    except pymssql.Error as e:
        LOGGER.exception("SQL CMD Error : %s", sqlcmd)
        LOGGER.exception("sql_SelectRowCount Function Error : %s", e)
        return str(e)
    finally:
        if conn != None:
            cursor.close()
            conn.close()
    return


### 執行 SQL insert, update, delete
def sql_RunCmd(sqlcmd):
    try:
        conn = GetDBConnect()
        cursor = conn.cursor(as_dict=True)
        cursor.execute(sqlcmd)
        conn.commit()
        return True
    except pymssql.Error as e:
        conn.rollback()
        LOGGER.exception("SQL CMD Error : %s", sqlcmd)
        LOGGER.exception("sql_RunCmd Function Error : %s", e)
        return str(e)
    finally:
        if conn != None:
            cursor.close()
            conn.close()
    return


### 針對 DB and Table Structure 執行
def sql_RunSchemaCmd(sqlcmd):
    try:
        conn = GetDBConnect()
        cursor = conn.cursor()
        conn.autocommit(True)   #指令立即执行，無需等待 conn.commit()
        cursor.execute(sqlcmd)
        conn.autocommit(False)
        return True
    except pymssql.Error as e:
        conn.rollback()
        LOGGER.exception("SQL CMD Error : %s", sqlcmd)
        LOGGER.exception("sql_RunCmd Function Error : %s", e)
        return str(e)
    finally:
        if conn != None:
            cursor.close()
            conn.close()
    return


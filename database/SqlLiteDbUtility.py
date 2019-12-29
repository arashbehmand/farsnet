class SqlLiteDbUtility(object):
    """ generated source for class SqlLiteDbUtility """

    connection = None

    @classmethod
    def getConnection(cls):
        """ generated source for method getConnection """
        if cls.connection != None:
            return cls.connection
        try:
            Class.forName("org.sqlite.JDBC")
            cls.connection = DriverManager.getConnection(
                "jdbc:sqlite:" + dbfile.getAbsolutePath() + "/farsnet2.5.db3"
            )
            print dbfile.getAbsolutePath()
        except Exception as e:
            e.printStackTrace()
        return cls.connection

#!/usr/bin/python3
def get_response(environ, start_response, app_config, message):
    if environ:
        pass  # Lets ignore not usage PyCharm
    start_response('404 Not found', [('Content-Type', 'text/html; charset=utf-8')])
    return [
        bytes(
            (
                """
                <!DOCTYPE html>
                <html>
                <head>
                    <meta charset="UTF-8">
                    <title>404 Error</title>
                </head>
                <body>
                    <h1>
                        <center>
                            <font 
                                color="green">In[0]:</font>
                            <font 
                                color="#8333ff">sum</font>([item*<font color="blue">10</font>**i 
                            <font 
                                color="orange">for</font>
                            i<font color="orange">,</font> item <font color="orange">in</font> 
                            <font color="#8333ff">enumerate</font>
                            ([<font color="blue">2</font> ** <font color="blue">2</font><font color="orange">,</font> 
                            <font
                                color="blue">0</font> * <font color="blue">0</font> ** <font color="blue">0</font><font
                                color="orange">,</font> <font
                                color="blue">2</font> ** <font color="blue">2</font>])])
                        </center>
                    </h1>
                    <center>
                    <p><b><u>Application</u></b>: <i>"%s"</i></p>
                    <p><b><u>Message</u></b>: "%s"</p>
                    <p>...go to <a href="/">start</a> page.</p>
                    </center>
                </body>
                </html>
                """
            ) % (
                app_config.APP_NAME,
                message,
            )
            , 'utf-8'
        )
    ]

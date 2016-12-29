

def bake_email_template(email_addr,msg):
    html = """
    <html xmlns="http://www.w3.org/1999/xhtml">

<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0;">
    <style>
    /* Reset styles */
    
    body {
        margin: 0;
        padding: 0;
        min-width: 100%;
        width: 100% !important;
        height: 100% !important;
    }
    
    body,
    table,
    td,
    div,
    p,
    a {
        -webkit-font-smoothing: antialiased;
        text-size-adjust: 100%;
        -ms-text-size-adjust: 100%;
        -webkit-text-size-adjust: 100%;
        line-height: 100%;
    }
    
    table,
    td {
        mso-table-lspace: 0pt;
        mso-table-rspace: 0pt;
        border-collapse: collapse !important;
        border-spacing: 0;
    }
     
    img {
        border: 0;
        line-height: 100%;
        outline: none;
        text-decoration: none;
        -ms-interpolation-mode: bicubic;
    }
    
    #outlook a {
        padding: 0;
    }
    
    .ReadMsgBody {
        width: 100%;
    }
    
    .ExternalClass {
        width: 100%;
    }
    
    .ExternalClass,
    .ExternalClass p,
    .ExternalClass span,
    .ExternalClass font,
    .ExternalClass td,
    .ExternalClass div {
        line-height: 100%;
    }
    /* Rounded corners for advanced mail clients only */
    
    @media all and (min-width: 560px) {
        .container {
            border-radius: 8px;
            -webkit-border-radius: 8px;
            -moz-border-radius: 8px;
            -khtml-border-radius: 8px;
        }
    }
    /* Set color for auto links (addresses, dates, etc.) */
    
    a,
    a:hover {
        color: #127DB3;
    }
    
    .footer a,
    .footer a:hover {
        color: #999999;
    }
    
    .customTable {
        border-collapse: collapse;
        display: inline-block;
        width: 100%;
        margin: 20px 0px;
    }
    
    .customTable th,
    .customTable td {
        font-size: 12px;
        padding: 7px;
    }
    
    .customTable th,
    .customTable td {
        border-bottom: 1px solid #ddd;
        border-top: 1px solid #ddd;
        border-left: 1px solid #ddd;
        border-right: 1px solid #ddd;
        text-align: center;
        width: 200px;
    }
    
    .customTable tr:nth-child(even) {
        background-color: #f2f2f2
    }
    
    .customTable th {
        background-color: #4CAF50;
        color: white;
        width: 200px;
    }
    </style>
    <!-- MESSAGE SUBJECT -->
    <title>GetGrub Verify Email</title>
</head>
<!-- BODY -->
<!-- Set message background color (twice) and text color (twice) -->
#009587
<body topmargin="0" rightmargin="0" bottommargin="0" leftmargin="0" marginwidth="0" marginheight="0" width="100%" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; width: 100%; height: 100%; -webkit-font-smoothing: antialiased; text-size-adjust: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; line-height: 100%;
        background-color: #FFFFFF;
        color: #000000;" bgcolor="#ffffff" text="#000000">
    <!-- SECTION / BACKGROUND -->
    <!-- Set message background color one again -->
    <table bgcolor="#009587"width="100%" align="center" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; width: 100%;" class="background">
        <tr>
            <td align="center" valign="top" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0;" bgcolor="#FFFFFF">
                <!-- WRAPPER -->
                <!-- Set wrapper width (twice) -->
                <table border="0" cellpadding="0" cellspacing="0" align="center" width="560" style="border-collapse: collapse; border-spacing: 0; padding: 0; width: inherit;
                max-width: 560px;" class="wrapper">
                    <tr>
                        <td align="left" valign="top" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; padding-left: 6.25%; padding-right: 6.25%; width: 87.5%;
                        padding-top: 0px;
                        padding-bottom: 0px;">
                            <!-- PREHEADER -->
                            <!-- Set text color to background color -->
                            <!-- LOGO -->
                            <!-- Image text color should be opposite to background color. Set your url, image src, alt and title. Alt text should fit the image size. Real image size should be x2. URL format: http://domain.com/?utm_source={{Campaign-Source}}&utm_medium=email&utm_content=logo&utm_campaign={{Campaign-Name}} -->
                            <!--a target="_blank" style="text-decoration: none;" href="http://www.getgrub.in"><img border="0" vspace="0" hspace="0" src="https://avatars1.githubusercontent.com/u/22232404?v=3&s=200" width="70" height="70" alt=" " title="GetGrub" style="
                            color: #000000;
                        font-size: 10px; margin: 13; padding: 0; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; border: none; display: block;" /></a>-->
                        </td>
                    </tr>
                    <!-- End of WRAPPER -->
                </table>
                <!-- WRAPPER / CONTEINER -->
                <!-- Set conteiner background color -->
                <table border="0" cellpadding="0" cellspacing="0" align="center" bgcolor="#009587" width="560" style="border-collapse: collapse; border-spacing: 0; padding: 0; width: inherit;
                max-width: 560px;" class="container">
                    <!-- <tr>
                        <td align="center" valign="top" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0;
                                padding-top: 20px;" class="hero">
                            <a target="_blank" style="text-decoration: none;" href="http://www.getgrub.in">
                                <img border="0" vspace="0" hspace="0" src="http://getgrub.in/img/getgrublogo.png" alt='' width="560" style="width: 100%; max-width: 560px; color: #000000; font-size: 13px; margin: 0; padding: 0; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; border: none; display: block;" />
                            </a>
                        </td>
                    </tr> -->
                    <tr>
                        <td align="left" valign="top" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; padding-left: 6.25%; padding-right: 6.25%; width: 87.5%; font-size: 15px; font-weight: 400; line-height: 160%;
                            padding-top: 25px;
                            color: #FFFFFF;
                            font-family: Helvetica Neue Light,Helvetica Regular,Arial,sans-serif;" class="paragraph">
                            <a target="_blank" style="text-decoration: none;" href="http://www.printhen.com"><img border="0" vspace="0" hspace="0" src="https://avatars1.githubusercontent.com/u/22232404?v=3&s=200" width="70" height="70" alt=" " title="PrintHen" style="
                            color: #000000;
                        font-size: 10px; margin: 13; float:right; padding: 0; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; border: none; display: block;" /></a>
                        
                            <span style="font-size:1.5em"><b color="#FFFFFF">Dear """+ name """, </b></span>
                            <br>
                            
                            <br> <b> Greetings from Printhen</b> 
                            <br>
                            <br> """ + msg
                            """
                            <br>
                            <br>
                            <br>
                            <table align="center" cellspacing="0" cellpadding="0">
                                <tr>
                                    <td align="center" width="300" height="40" bgcolor="#009587" style="-webkit-border-radius: 5px; -moz-border-radius: 5px; border-radius: 5px; color: #ffffff; display: block;">
                                        <a href="http://printhen.com" style="color:#000000;text-decoration:none;outline-style:none" target="_blank">
                                            <span style="background-color:#FFC006;padding-top:15px;padding-bottom:15px;padding-right:30px;padding-left:30px;border-radius:7px">Visit Printhen</span>
                                        </a>
                                    </td>
                                </tr>
                            </table>
                           <!-- <font color="#333333">                                
                           <center>
                                    <font face="Helvetica Neue Light,Helvetica Regular,Arial,sans-serif" size="3"><i>
                                    Wanna grab a delicious Pizza?<br></i>
                                    </font>
                                </center>
                            </font> -->
                            <br> <b>Regards,
                            <br> Printhen Team</b>
                        </td>
                    </tr>
                    <tr>
                        <td align="center" valign="top" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; padding-left: 6.25%; padding-right: 6.25%; width: 87.5%;
                                padding-top: 25px;" class="line">
                            <hr color="#E0E0E0" align="center" width="100%" size="1" noshade style="margin: 0; padding: 0;" />
                        </td>
                    </tr>
                    <!-- PARAGRAPH -->
                    <!-- Set text color and font family ("sans-serif" or "Georgia, serif"). Duplicate all text styles in links, including line-height -->
                    <tr>
                        <td align="center" valign="top" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; padding-left: 6.25%; padding-right: 6.25%; width: 87.5%; font-size: 13px; font-weight: 400; line-height: 160%;
                                padding-top: 20px;
                                padding-bottom: 25px;
                                color: #000000;
                                font-family: sans-serif;" class="paragraph">
                            Have a&nbsp;question? Send a word to
                            <a href="mailto:info@printhen.com" target="_blank" style="text-decoration:none;color: #127DB3; font-family: sans-serif; font-size: 13px; font-weight: 400; line-height: 160%;">info@printhen.com</a>
                        </td>
                    </tr>
                    <!-- End of WRAPPER -->
                </table>
                <!-- WRAPPER -->
                <!-- Set wrapper width (twice) -->
            </td>
        </tr>
    </table>
</body>

</html>

"""
    return html
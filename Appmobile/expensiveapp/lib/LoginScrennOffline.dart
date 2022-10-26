import 'package:expensiveapp/FindAccount.dart';
import 'package:expensiveapp/FindAccountOffline.dart';
import 'package:expensiveapp/SignupScreen.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';


class LoginScreenOffline extends StatefulWidget {
  const LoginScreenOffline({super.key});

  @override
  State<LoginScreenOffline> createState() => _LoginScreenOfflineState();
}

class _LoginScreenOfflineState extends State<LoginScreenOffline> {
  bool isRemberMe = false;
  Widget buildUsername() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        Text(
          'Username',
          style: TextStyle(
              color: Colors.white, fontSize: 16, fontWeight: FontWeight.bold),
        ),
        SizedBox(height: 10),
        Container(
          alignment: Alignment.centerLeft,
          decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(10),
              boxShadow: [
                BoxShadow(
                    color: Colors.black26, blurRadius: 6, offset: Offset(0, 2)),
              ]),
          height: 60,
          child: TextField(
            keyboardType: TextInputType.emailAddress,
            style: TextStyle(color: Colors.black87),
            decoration: InputDecoration(
                border: InputBorder.none,
                contentPadding: EdgeInsets.only(top: 14),
                prefixIcon: Icon(
                  Icons.account_circle,
                  color: Color.fromARGB(255, 54, 6, 226),
                ),
                hintText: 'Username',
                hintStyle: TextStyle(color: Colors.black38)),
          ),
        )
      ],
    );
  }

  Widget builPassword() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        Text(
          'Password',
          style: TextStyle(
              color: Colors.white, fontSize: 16, fontWeight: FontWeight.bold),
        ),
        SizedBox(height: 10),
        Container(
          alignment: Alignment.centerLeft,
          decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(10),
              boxShadow: [
                BoxShadow(
                    color: Colors.black26, blurRadius: 6, offset: Offset(0, 2)),
              ]),
          height: 60,
          child: TextField(
            obscureText: true,
            style: TextStyle(color: Colors.black87),
            decoration: InputDecoration(
                border: InputBorder.none,
                contentPadding: EdgeInsets.only(top: 14),
                prefixIcon: Icon(
                  Icons.lock,
                  color: Color.fromARGB(255, 54, 6, 226),
                ),
                hintText: 'Password',
                hintStyle: TextStyle(color: Colors.black38)),
          ),
        )
      ],
    );
  }

  Widget buildForgetPassBtn() {
    return Container(
      alignment: Alignment.bottomCenter,
      child: TextButton(
        onPressed: () => Navigator.push(
            context, MaterialPageRoute(builder: (_) => const FindAccountOffline())),
        child: Text(
          'Forget Password ?',
          style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
        ),
      ),
    );
  }

  Widget buildRememberCb() {
    return Container(
      height: 20,
      child: Row(
        children: <Widget>[
          Theme(
              data: ThemeData(unselectedWidgetColor: Colors.white),
              child: Checkbox(
                value: isRemberMe,
                checkColor: Colors.green,
                activeColor: Colors.white,
                onChanged: (value) {
                  setState(() {
                    isRemberMe = value!;
                  });
                },
              )),
          Text(
            'Remember me ',
            style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
          )
        ],
      ),
    );
  }

  Widget buildLoginBtn() {
    return Container(
        padding: EdgeInsets.symmetric(vertical: 25),
        width: double.infinity,
        child: ElevatedButton(
          style: ElevatedButton.styleFrom(
              primary: Colors.white, // background
              onPrimary: Colors.white, // foreground
              padding: EdgeInsets.all(15),
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(15))),
          onPressed: () => print('login Pressed'),
          child: Text(
            'Login',
            style: TextStyle(
                color: Color.fromARGB(255, 54, 6, 226),
                fontSize: 18,
                fontWeight: FontWeight.bold),
          ),
        ));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: AnnotatedRegion<SystemUiOverlayStyle>(
        value: SystemUiOverlayStyle.light,
        child: GestureDetector(
          child: Stack(
            children: <Widget>[
              Container(
                  height: double.infinity,
                  width: double.infinity,
                  decoration: BoxDecoration(
                      color: const Color(0xff7c94b6),
                      image: DecorationImage(
                        image: new AssetImage("assets/images/expensess.png"),
                        alignment: Alignment.topCenter,
                        colorFilter: ColorFilter.mode(
                            Color.fromARGB(65, 48, 22, 214).withOpacity(0.4),
                            BlendMode.dstATop),
                      ),
                      gradient: LinearGradient(
                          begin: Alignment.bottomCenter,
                          end: Alignment.topCenter,
                          colors: [
                            Color.fromARGB(102, 2, 15, 56),
                            Color.fromARGB(153, 12, 44, 140),
                            Color.fromARGB(204, 7, 42, 148),
                            Color.fromARGB(255, 65, 108, 238),
                          ])),
                  child: SingleChildScrollView(
                    physics: AlwaysScrollableScrollPhysics(),
                    padding:
                        EdgeInsets.symmetric(horizontal: 25, vertical: 120),
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: <Widget>[
                        Text(
                          'LogIn',
                          style: TextStyle(
                            color: Colors.white,
                            fontSize: 40,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                        SizedBox(height: 50),
                        buildUsername(),
                        SizedBox(height: 20),
                        builPassword(),
                        SizedBox(height: 20),
                        buildRememberCb(),
                        buildLoginBtn(),
                        buildForgetPassBtn(),
                      ],
                    ),
                  ))
            ],
          ),
        ),
      ),
    );
  }
}

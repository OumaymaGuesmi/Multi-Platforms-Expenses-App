import 'package:expensiveapp/LoginScreen.dart';
import 'package:expensiveapp/LoginScrennOffline.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'dart:math';

class SignUpScreenOffline extends StatefulWidget {
  const SignUpScreenOffline({super.key});

  @override
  State<SignUpScreenOffline> createState() => _SignUpScreenOfflineState();
}

class _SignUpScreenOfflineState extends State<SignUpScreenOffline> {
  bool isRemberMe = false;
  bool isRemberMe1 = false;
  int intValue = 0;
  Widget buildusername() {
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
            keyboardType: TextInputType.text,
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

  Widget builConfirmPassword() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        Text(
          'Confirm Password',
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

  void _generateRandomNumber1() {
    setState(() {
      intValue = Random().nextInt(10); // Value is >= 0 and < 10.
      intValue = Random().nextInt(100) + 50;
    });
    // Value is >= 50 and < 150.
  }

  Widget buildgeneratecodepin() {
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
                    print(intValue);
                    print(value);
                    if (isRemberMe == true) {
                      print(isRemberMe);
                      _generateRandomNumber1();
                    }
                  });
                },
              )),
          Text(
            'Generate code pin ',
            style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
          ),
        ],
      ),
    );
  }

  Widget generateBtn() {
    return isRemberMe
        ? Container(
            padding: EdgeInsets.symmetric(vertical: 25),
            width: double.infinity,
            child: ElevatedButton(
              style: ElevatedButton.styleFrom(
                  primary: Colors.white, // background
                  onPrimary: Colors.white, // foreground
                  padding: EdgeInsets.all(15),
                  shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(15))),
              onPressed: () => print('Singup Pressed'),
              child: Text(
                '$intValue',
                style: TextStyle(
                  color: Color.fromARGB(255, 12, 12, 12),
                  fontSize: 40,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ))
        : SizedBox();
  }

  Widget buildentercodepin() {
    return Container(
      height: 20,
      child: Row(
        children: <Widget>[
          Theme(
              data: ThemeData(unselectedWidgetColor: Colors.white),
              child: Checkbox(
                value: isRemberMe1,
                checkColor: Colors.green,
                activeColor: Colors.white,
                onChanged: (value) {
                  setState(() {
                    isRemberMe1 = value!;
                  });
                },
              )),
          Text(
            'Enter your code pin ',
            style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
          ),
        ],
      ),
    );
  }

  Widget generatecodeBtn() {
    return isRemberMe1
        ? Container(
            padding: EdgeInsets.symmetric(vertical: 25),
            width: double.infinity,
            child: ElevatedButton(
                style: ElevatedButton.styleFrom(
                    primary: Colors.white, // background
                    onPrimary: Colors.white, // foreground
                    padding: EdgeInsets.all(15),
                    shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(15))),
                onPressed: () => print('Singup Pressed'),
                child: TextField(
                  decoration: InputDecoration(labelText: 'Enter Number'),
                  keyboardType: TextInputType.numberWithOptions(decimal: true),
                  inputFormatters: [
                    FilteringTextInputFormatter.allow(RegExp('[0-9.,]')),
                  ],
                )))
        : SizedBox();
  }

  Widget buildSignupBtn() {
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
          onPressed: () => Navigator.push(context,
              MaterialPageRoute(builder: (_) => const LoginScreenOffline())),
          child: Text(
            'Sign Up',
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
                        image: new AssetImage("assets/images/value.png"),
                        alignment: Alignment.topCenter,
                        colorFilter: ColorFilter.mode(
                            Color.fromARGB(65, 48, 22, 214).withOpacity(0.4),
                            BlendMode.dstATop),
                      ),
                      gradient: LinearGradient(
                          begin: Alignment.topCenter,
                          end: Alignment.bottomCenter,
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
                          'Sign Up',
                          style: TextStyle(
                            color: Colors.white,
                            fontSize: 40,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                        SizedBox(height: 10),
                        buildusername(),
                        SizedBox(height: 10),
                        builPassword(),
                        SizedBox(height: 10),
                        builConfirmPassword(),
                        SizedBox(height: 10),
                        buildgeneratecodepin(),
                        SizedBox(height: 20),
                        buildentercodepin(),
                        SizedBox(height: 20),
                        generateBtn(),
                        SizedBox(height: 5),
                        generatecodeBtn(),
                        buildSignupBtn(),
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

import 'package:expensiveapp/SignupScreen.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class FindAccountOffline extends StatefulWidget {
  const FindAccountOffline({super.key});

  @override
  State<FindAccountOffline> createState() => _FindAccountOfflineState();
}

class _FindAccountOfflineState extends State<FindAccountOffline> {
  bool isRemberMe = false;
  Widget buildEmail() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        Text(
          'Enter your Pin',
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
                  decoration: InputDecoration(),
                  keyboardType: TextInputType.numberWithOptions(decimal: true),
                  inputFormatters: [
                    FilteringTextInputFormatter.allow(RegExp('[0-9.,]')),
                  ],
)
        )
      ],
    );
  }

  Widget buildSendPinBtn() {
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
            'Confirm',
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
                            Color.fromARGB(65, 40, 10, 235).withOpacity(0.4),
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
                        EdgeInsets.symmetric(horizontal: 25, vertical: 220),
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: <Widget>[
                        Text(
                          'Access your account',
                          style: TextStyle(
                              color: Colors.white,
                              fontSize: 30,
                              fontWeight: FontWeight.bold,
                              ),
                        ),
                        SizedBox(height: 20),
                        buildEmail(),
                        SizedBox(height: 20),
                        buildSendPinBtn(),
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

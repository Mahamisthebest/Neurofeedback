// Your web app's Firebase configuration get it from your firebase project
/*
var firebaseConfig = {
  apiKey: "AIzaSyAJEQRrPcBainTEtz5R4bwV9y1k7FBGCjM",
  authDomain: "pythontojs-cbbcc.firebaseapp.com",
  databaseURL: "https://pythontojs-cbbcc.firebaseio.com",
  projectId: "pythontojs-cbbcc",
  storageBucket: "pythontojs-cbbcc.appspot.com",
  messagingSenderId: "836687372065",
  appId: "1:836687372065:web:467f3db67ad75cde0d2860",
  measurementId: "G-JRH8CV4MZ0"
};*/
var firebaseConfig = {
  apiKey: "AIzaSyBnURgo05_V0c3FdrXTR0ptg3Mhva2hSOs",
  authDomain: "pythontojs-b1623.firebaseapp.com",
  databaseURL: "https://pythontojs-b1623.firebaseio.com",
  projectId: "pythontojs-b1623",
  storageBucket: "pythontojs-b1623.appspot.com",
  messagingSenderId: "1068624202322",
  appId: "1:1068624202322:web:25417fa31bc0e6702bad8b"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
//firebase.analytics();

//get value for band channel and threshold from url
var url_string = window.location;
var url = new URL(url_string);
var band = url.searchParams.get('band');
var channel = url.searchParams.get('channel');
var thresh = url.searchParams.get('thresh');

console.log(band + '  ' + channel + '  ' + thresh);

//mention reference to the database in firebase that was created by python file
var dbRef = firebase.database().ref();
//table name that is in the firebase db
var bandsRef = dbRef.child('Data');

//next button for redirection on next page
var next = document.getElementById('next');

//listen for changes and get values whenever a new one was created in db
bandsRef.on('value', gotData, errData);

//initialize numerals to identify each bands in db as defined in db
if (band == 'theta') {
  band = 1;
}

if (band == 'alpha') {
  band = 2;
}

if (band == 'beta') {
  band = 4;
}

if (band == 'gamma') {
  band = 6;
}

if (band == 'delta') {
  band = 0;
}

if (band == 'highbeta') {
  band = 5;
}
if (band == 'smr') {
  band = 3;
}
//next button function to delete from db using 'del' function
next.addEventListener('click', del);

//get respective data from db
function gotData(data) {
  //get all the data from db
  var all_data = data.val();
  //get keys for each data
  var keys = Object.keys(all_data);
  //loop in keys to get respective data of the band and its channel
  for (var i = 0; i < keys.length; i++) {
    var k = keys[i];

    //compare the 'channel' from url to the numerals and then get the respective table value
    if (channel == 1) {
      var val = all_data[k].Channel_1;
    }
    if (channel == 2) {
      var val = all_data[k].Channel_2;
    }
    if (channel == 3) {
      var val = all_data[k].Channel_3;
    }
    if (channel == 4) {
      var val = all_data[k].Channel_4;
    }
    if (channel == 5) {
      var val = all_data[k].Channel_5;
    }
    if (channel == 6) {
      var val = all_data[k].Channel_6;
    }
    if (channel == 7) {
      var val = all_data[k].Channel_7;
    }
    if (channel == 8) {
      var val = all_data[k].Channel_8;
    }
    if (channel == 9) {
      var val = all_data[k].Channel_9;
    }
    if (channel == 10) {
      var val = all_data[k].Channel_10;
    }
    if (channel == 11) {
      var val = all_data[k].Channel_11;
    }
    if (channel == 12) {
      var val = all_data[k].Channel_12;
    }
    if (channel == 13) {
      var val = all_data[k].Channel_13;
    }
    if (channel == 14) {
      var val = all_data[k].Channel_14;
    }
  console.log(val[band]);
    //pass values of respective band number and threshold to the function
  toggleVideoState(val[band], thresh);
 }
   
}

//logs error if any
function errData(data) {
  console.log('Error!' + err);
}

//delete data from firebase after session is completed
function del() {
  bandsRef.remove();
  //remove this file if no need to keep enumerated files of session
  window.location.href = '../session/toMysql.php';
}

//get video tag
var vid = document.getElementById('myVideo');

//this function play and pause values by comparing it to threshold and the values got from db
function toggleVideoState(values, threshold) {
  if (vid.paused && values > threshold) {
    vid.play();
    console.log('Video Playing');
  } 
  else {
    vid.pause();
    console.log('Video Paused');
  }
}

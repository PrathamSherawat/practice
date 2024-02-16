// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyB8XjqPuJJDMuPvFRREAlGrHml80d_mgDE",
  authDomain: "react-project-2d052.firebaseapp.com",
  projectId: "react-project-2d052",
  storageBucket: "react-project-2d052.appspot.com",
  messagingSenderId: "486536859098",
  appId: "1:486536859098:web:c61bad26dcdbb57f65c4e3",
  measurementId: "G-SVCS49TSKV"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
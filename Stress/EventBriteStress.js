import http from 'k6/http';
import { sleep } from 'k6';
import { check } from 'k6';
import urlencode from 'https://jslib.k6.io/form-urlencoded/3.0.0/index.js';
export let options = {
    insecureSkipTLSVerify: true,
    noConnectionReuse: false,
    thresholds: {
        http_req_duration: ['p(80)<2000'] 
    },
    stages: [
        // Below average load
        { duration: '30s', target: 80 },  // raises users from 0 to 80 in 20 seconds
        { duration: '30s', target: 80 },  // keeps users at that number for 20 seconds

        // Average load        
        { duration: '30s', target: 120 },  // raises users from 80 to 120 in 20 seconds
        { duration: '30s', target: 120 },  // keeps users at that number for 20 seconds

        // Server starts giving errors at around 140-150

        // Above average load (server about to shut down)
        { duration: '30s', target: 175 },  // raises users from 120 to 175 in 20 seconds
        { duration: '30s', target: 175 },  // keeps users at that number for 20 seconds

        // // This is even going further beyond
        { duration: '30s', target: 200 },  // raises users from 175 to 200 in 20 seconds
        { duration: '30s', target: 200 },  // keeps users at that number for 20 seconds

        // // Recovery stage
        { duration: '4m', target: 0 },  // returns to 0 users.

    ],
    // vus :1,
    // duration: '10s'
};

const API_BASE_URL = 'http://44.210.36.161:5000';
const requestHeaders = {     
        'Authorization': 'Bearer '+'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdGFydCI6MTY4NDAyMjMxOS41NDQ5MjcsImV4cCI6MTY4NDEwODcxOSwiaWQiOiI2NDVhNWQyMDM0NDA4ZTczM2JhNTY5OTYiLCJlbWFpbCI6ImFobWVkc2FhZF8yMDA5QGxpdmUuY29tIn0.Qvfms7vkVSVxlRlMDr0HBL9B-hO3Rq7jc4Hz2noXTsI', // ahmed saad token :))
};
// var data = '';


export default () => {

    const responses = []
    let params = { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } }
    let payload = {
        username: "ahmedsaad_2009@live.com",
        password: "123456789" ,
    };
    let resp = http.post(API_BASE_URL+'/auth/login', payload, params);
    responses.push(resp)
    // console.log(resp.body)

    let catReq = { method: 'GET', url: API_BASE_URL+'/categories/', params: { headers: requestHeaders } }
    let res = http.get(API_BASE_URL+'/categories/')

    check(res, {
        'is status 200': (r) => r.status === 200
    });

    let categoryName = "Sports & Fitness"
    let getCategoryByName = { method: 'GET', url: API_BASE_URL+'/categories/'+categoryName, 
        params: { headers: requestHeaders } 
    }

    let getCategorySubCategories = { method: 'GET', url: API_BASE_URL+'/categories/'+categoryName+"/sub_categories", 
    params: { headers: requestHeaders } 
    }

    let email = "ahmedsaad_2009@live.com"
    let checkEmail = { method: 'GET', url: API_BASE_URL+'/users/emails/check?email='+email, 
        params: { headers: requestHeaders } 
    }

    let getAvatar = { method: 'GET', url: API_BASE_URL+'/users/email/info/avatar?email='+email, 
        params: { headers: requestHeaders } 
    }

    let userInfo = { method: 'GET', url: API_BASE_URL+'/users/me/info', 
    params: { headers: requestHeaders } 
    }
    // let idUser = userInfo

    let liked = { method: 'GET', url: API_BASE_URL+'/users/me/event/liked', 
    params: { headers: requestHeaders } 
    }

    let followingInfo = { method: 'GET', url: API_BASE_URL+'/users/me/user/following', 
    params: { headers: requestHeaders } 
    }

    let orders = { method: 'GET', url: API_BASE_URL+'/orders/myorders/', 
    params: { headers: requestHeaders } 
    }

    let isAuthorized = { method: 'PUT', url: API_BASE_URL+'/auth/verify-email/', 
    params: { headers: requestHeaders } 
    }

    // payload = {
    //     new_password : "123456789"
    // }
    // // let changePass = { method: 'PUT', url: API_BASE_URL+'/auth/change-password', 
    // // params: { headers: requestHeaders } , JS
    // // }

    // let result = http.put(API_BASE_URL+'/auth/change-password', payload, params);


    let eventsSearch = { method: 'GET', url: API_BASE_URL+'/events/search?city=Cairo', 
    params: { headers: requestHeaders } 
    }

    const requests = http.batch([
        catReq,getCategoryByName,getCategorySubCategories,checkEmail,getAvatar,userInfo,
        liked,followingInfo,orders,isAuthorized,eventsSearch
    ]);
    
    let idUser = null
    for (let i = 0 ; i < requests.length;i++){
        check(requests[i], {
            'is status 200': (r) => r.status === 200
        });
        if (i == 5){
            // console.log(requests[i].body)
            res = JSON.parse(requests[i].body)
            idUser = res.id
            // console.log(idUser)
        }
    }
    if (idUser != null){
        // console.log(idUser)
        // /users/id/{user_id}/info
        let response = http.get(API_BASE_URL+'/users/id/'+idUser+"/info")
        check(response, {
            'is status 200': (r) => r.status === 200
        });
    }




    // const requests_2 = http.batch([
    //     catReq,getCategoryByName,getCategorySubCategories,checkEmail,getAvatar,userInfo,
    //     liked,followingInfo
    // ]);
    // let body = urlencode({ username: "ahmedsaad_2009@live.com", password: "123456789" });
    
    params = { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } }
    payload = {
        username: "ahmedsaad_2009@live.com",
        password: "123456789" ,
    };
    resp = http.post(API_BASE_URL+'/auth/login', payload, params);
    responses.push(resp)
    // console.log(resp.body);
    payload = {
        username: "omar.sendiony@gmail.com",
        password: "123456789" ,
    }
    // resp =  http.post(API_BASE_URL+'/auth/login-with-google', payload, params);
    responses.push(resp)
    // console.log(resp.body);


    // forgettttttttttttttttt password //////////////
    // payload = {
    //     email: "omar.sendiony@gmail.com"
    // }
    // resp =  http.post(API_BASE_URL+'/auth/forgot-password', payload, params);
    // responses.push(resp)
    // console.log(resp.body);

    for (let i = 0 ; i < responses.length;i++){
        check(responses[i], {
            'is status 200': (r) => r.status === 200
        });
    }

    // check email



    sleep(2)
};
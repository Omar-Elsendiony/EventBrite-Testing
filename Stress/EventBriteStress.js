import http from 'k6/http';
import { sleep } from 'k6';
import { check } from 'k6';

export let options = {
    insecureSkipTLSVerify: true,
    noConnectionReuse: false,
    thresholds: {
        http_req_duration: ['p(95)<1000'] // el 1750 dyh milli seconds
                                         // checks if the fastest 90% have finished their requests in less than 1050 ms
    },
    stages: [
        // Below average load
        { duration: '2s', target: 1 },  // raises users from 0 to 80 in 20 seconds
        // { duration: '5s', target: 1 },  // keeps users at that number for 20 seconds

        // Average load        
        // { duration: '20s', target: 120 },  // raises users from 80 to 120 in 20 seconds
        // { duration: '20s', target: 120 },  // keeps users at that number for 20 seconds

        // // Server starts giving errors at around 140-150

        // // Above average load (server about to shut down)
        // { duration: '20s', target: 175 },  // raises users from 120 to 175 in 20 seconds
        // { duration: '20s', target: 175 },  // keeps users at that number for 20 seconds

        // // // This is even going further beyond
        // { duration: '20s', target: 200 },  // raises users from 175 to 200 in 20 seconds
        // { duration: '20s', target: 200 },  // keeps users at that number for 20 seconds

        // // Recovery stage
        // { duration: '3m', target: 0 },  // returns to 0 users.

    ],
    // vus :1,
    // duration: '10s'
};

const API_BASE_URL = 'http://44.210.36.161:5000';
const requestHeaders = {     
        'Authorization': 'Bearer '+'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdGFydCI6MTY4NDAwMTI2NS4wMTg2OTIsImV4cCI6MTY4NDA4NzY2NSwiaWQiOiI2NDVhNWQyMDM0NDA4ZTczM2JhNTY5OTYiLCJlbWFpbCI6ImFobWVkc2FhZF8yMDA5QGxpdmUuY29tIn0.c7L2VvRnHS_cyxrtHo5_CJ2N8-S33Iz7FL-8tqkinz8', // dh el token bta3 abosabry
};
// var data = '';


export default () => {
    let catReq = { method: 'GET', url: API_BASE_URL+'/categories/', params: { headers: requestHeaders } }
    let res = http.get(API_BASE_URL+'/categories/')

    check(res, {
        'is status 200': (r) => r.status === 200
    });
    // console.log(res.status)
    // let data = {

    // }

    // let createCat = { method: 'POST', url: API_BASE_URL+'/categories/', params: { headers: requestHeaders,body: } }

    let categoryName = "Sports & Fitness"
    let getCategoryByName = { method: 'GET', url: API_BASE_URL+'/categories/'+categoryName, 
        params: { headers: requestHeaders } 
    }

    let getCategorySubCategories = { method: 'GET', url: API_BASE_URL+'/categories/'+categoryName+"/sub_categories", 
    params: { headers: requestHeaders } 
    }

    const requests = http.batch([
        catReq,getCategoryByName,getCategorySubCategories
    ]);
    
    for (let i = 0 ; i < requests.length;i++){
        check(requests[i], {
            'is status 200': (r) => r.status === 200
        });
    }


    // const req3 = {
    //     method: 'POST',
    //     url: 'http://mysirius.me:3000/home/retweet',
    //     params: {
    //       headers: { 'Authorization': 'Bearer ' +'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYyOGQ5NzUwNGUyNjA1NzJjZGEzYWFlMyIsImlhdCI6MTY1MzQ0NjU0MywiZXhwIjoxNjYyMDg2NTQzfQ.c4KeGfQmkpir4L-nmPJpMgANjmhFhtXuD7LRSyoG6MU'},
    //       body: { tweetID: '6267e4828e27c30923a68588',},
    //     },
    //   };
    // const responses = http.batch([req3]);

    sleep(1)
};
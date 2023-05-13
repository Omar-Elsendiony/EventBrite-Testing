import http from 'k6/http';
import { sleep } from 'k6'
import { check } from 'k6'

export let options = {
    insecureSkipTLSVerify: true,
    noConnectionReuse: false,
    thresholds: {
        http_req_duration: ['p(90)<2750'] // el 1750 dyh milli seconds
                                         // checks if the fastest 90% have finished their requests in less than 1050 ms
    },
    stages: [
        // Below average load
        { duration: '5s', target: 1 },  // raises users from 0 to 80 in 20 seconds
 // returns to 0 users.

        // ebtada yedrab 3nd 145 mthln
    ],
};

const API_BASE_URL = 'http://test.k6.io';

const requestHeaders = {
        //'Authorization': 'Bearer ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYyNjQ5NzZiYjIwYzdhMjMzNDFhNGUxYiIsImlhdCI6MTY1MDkyNDg3NywiZXhwIjoxNjU5NTY0ODc3fQ.S1ZBOjDv6TcU48AEmn-8nHkgGiasZfj6Id2kk9ocYS4', // dh el token bta3 boody
        // 'Authorization': 'Bearer ' +'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYyNjg4ZWM5OWEzNjc3NWIzNDZlNmEyZCIsImlhdCI6MTY1MTAyMDMwNSwiZXhwIjoxNjU5NjYwMzA1fQ.nQusm1ETvwgOFceFbqu_BAG8F_uorveWD2LCGprh8pc', // dh el token bta3 user 0
        'Authorization': 'Bearer ' +'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYyOGQ5NzUwNGUyNjA1NzJjZGEzYWFlMyIsImlhdCI6MTY1MzQ0NjU0MywiZXhwIjoxNjYyMDg2NTQzfQ.c4KeGfQmkpir4L-nmPJpMgANjmhFhtXuD7LRSyoG6MU', // dh el token bta3 abosabry
};

export default () => {
    let res = http.get(API_BASE_URL);
    check(res, {
        'is status 200': (r) => r.status === 200
    });
    sleep(5)
};
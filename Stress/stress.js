import http from 'k6/http';
import { sleep } from 'k6'

export let options = {
    insecureSkipTLSVerify: true,
    noConnectionReuse: false,
    thresholds: {
        http_req_duration: ['p(95)<1000'] // el 1750 dyh milli seconds
                                         // checks if the fastest 90% have finished their requests in less than 1050 ms
    },
    stages: [
        // Below average load
        { duration: '20s', target: 80 },  // raises users from 0 to 80 in 20 seconds
        { duration: '20s', target: 80 },  // keeps users at that number for 20 seconds

        // Average load        
        { duration: '20s', target: 120 },  // raises users from 80 to 120 in 20 seconds
        { duration: '20s', target: 120 },  // keeps users at that number for 20 seconds

        // Server starts giving errors at around 140-150

        // Above average load (server about to shut down)
        { duration: '20s', target: 175 },  // raises users from 120 to 175 in 20 seconds
        { duration: '20s', target: 175 },  // keeps users at that number for 20 seconds

        // // This is even going further beyond
        { duration: '20s', target: 200 },  // raises users from 175 to 200 in 20 seconds
        { duration: '20s', target: 200 },  // keeps users at that number for 20 seconds

        // Recovery stage
        { duration: '3m', target: 0 },  // returns to 0 users.

        // ebtada yedrab 3nd 145 mthln
    ],
};

const API_BASE_URL = 'http://mysirius.me:3000';
const requestHeaders = {
        //'Authorization': 'Bearer ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYyNjQ5NzZiYjIwYzdhMjMzNDFhNGUxYiIsImlhdCI6MTY1MDkyNDg3NywiZXhwIjoxNjU5NTY0ODc3fQ.S1ZBOjDv6TcU48AEmn-8nHkgGiasZfj6Id2kk9ocYS4', // dh el token bta3 boody
        // 'Authorization': 'Bearer ' +'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYyNjg4ZWM5OWEzNjc3NWIzNDZlNmEyZCIsImlhdCI6MTY1MTAyMDMwNSwiZXhwIjoxNjU5NjYwMzA1fQ.nQusm1ETvwgOFceFbqu_BAG8F_uorveWD2LCGprh8pc', // dh el token bta3 user 0
        'Authorization': 'Bearer ' +'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYyOGQ5NzUwNGUyNjA1NzJjZGEzYWFlMyIsImlhdCI6MTY1MzQ0NjU0MywiZXhwIjoxNjYyMDg2NTQzfQ.c4KeGfQmkpir4L-nmPJpMgANjmhFhtXuD7LRSyoG6MU', // dh el token bta3 abosabry
};
// var data = '';


export default () => {

    
    const res = http.batch([
        { method: 'GET', url: API_BASE_URL+'/user0', params: { headers: requestHeaders } },
        { method: 'GET', url: API_BASE_URL+'/settings/profile', params: { headers: requestHeaders } },
        { method: 'GET', url: API_BASE_URL+'/user1', params: { headers: requestHeaders } },
        

        { method: 'GET', url: API_BASE_URL+'/home/:tweetId/likeTweet', params: { headers: requestHeaders } },        
        { method: 'GET', url: API_BASE_URL+'/home/', params: { headers: requestHeaders } },

        { method: 'GET', url: API_BASE_URL+'/home/:tweetId/getRetweeters', params: { headers: requestHeaders } },
        { method: 'GET', url: API_BASE_URL+'/home/getRetweets', params: { headers: requestHeaders } },
        { method: 'GET', url: API_BASE_URL+'/home/:tweetId/getLikers', params: { headers: requestHeaders } },       
        { method: 'GET', url: API_BASE_URL+'/home/:tweetId/getTaggedUsers', params: { headers: requestHeaders } },

        { method: 'GET', url: API_BASE_URL+'/home/:tweetId/getReplies', params: { headers: requestHeaders } },
        { method: 'GET', url: API_BASE_URL+'/settings/profile', params: { headers: requestHeaders } },
        { method: 'GET', url: API_BASE_URL+'/Boody', params: { headers: requestHeaders } },     
        { method: 'GET', url: API_BASE_URL+'/boody', params: { headers: requestHeaders } },         

        { method: 'GET', url: API_BASE_URL+'/search?q=bo&f', params: { headers: requestHeaders } },
        { method: 'GET', url: API_BASE_URL+'/admin/user', params: { headers: requestHeaders } },
        { method: 'GET', url: API_BASE_URL+'/home/6284d3df0ae56f80a9e9b098/quoteRetweet', params: { headers: requestHeaders } },    
        { method: 'GET', url: API_BASE_URL+'/home/getNotifications', params: { headers: requestHeaders } },     

        { method: 'GET', url: API_BASE_URL+'/home/628527e56cd229f25b32f047/getTweetById', params: { headers: requestHeaders } },   
        { method: 'GET', url: API_BASE_URL+'/settings/Deactivate-account', params: { headers: requestHeaders } },      
        { method: 'GET', url: API_BASE_URL+'/explore', params: { headers: requestHeaders } },       
        { method: 'GET', url: API_BASE_URL+'/explore/3aaaaaa', params: { headers: requestHeaders } },      

        { method: 'GET', url: API_BASE_URL+'/home/bookmarkedTweets', params: { headers: requestHeaders } },   
        { method: 'GET', url: API_BASE_URL+'/home/Follow-requests', params: { headers: requestHeaders } },    
        { method: 'GET', url: API_BASE_URL+'/home/Who-to-follow', params: { headers: requestHeaders } },      
        { method: 'GET', url: API_BASE_URL+'/messages/MohamedNano', params: { headers: requestHeaders } },    
        
        
        
        { method: 'POST', url: API_BASE_URL+'/signup', params: { headers: requestHeaders} },
        { method: 'POST', url: API_BASE_URL+'/login', params: { headers: requestHeaders} },
        
        { method: 'POST', url: API_BASE_URL+'/forgot-password', params: { headers: requestHeaders} },
        { method: 'POST', url: API_BASE_URL+'/home/retweet', params: { headers: requestHeaders} },
        ///////////{ method: 'POST', url: API_BASE_URL+'/home/retweet', params: { headers: requestHeaders}, data: data },
        { method: 'POST', url: API_BASE_URL+'/home/reply', params: { headers: requestHeaders} },
        { method: 'POST', url: API_BASE_URL+'/home/:tweetId/makePollChoice', params: { headers: requestHeaders} },

        { method: 'POST', url: API_BASE_URL+'/home/:tweetId/bookmarkTweet', params: { headers: requestHeaders} },
        { method: 'POST', url: API_BASE_URL+'/Boody/follow', params: { headers: requestHeaders} },
        { method: 'POST', url: API_BASE_URL+'/home/Follow-requests/accept', params: { headers: requestHeaders} },
        { method: 'POST', url: API_BASE_URL+'/messages/Ahmed', params: { headers: requestHeaders} },

        { method: 'DELETE', url: API_BASE_URL+'/home/62852cdd59b350aee60e4002/deleteNotification', params: { headers: requestHeaders} },
        { method: 'DELETE', url: API_BASE_URL+'/home/:tweetId/deleteTweet', params: { headers: requestHeaders} },
        
        { method: 'DELETE', url: API_BASE_URL+'/home/deleteBookmarkedTweets', params: { headers: requestHeaders} },
        { method: 'DELETE', url: API_BASE_URL+'/Boody/unfollow', params: { headers: requestHeaders} },
        { method: 'DELETE', url: API_BASE_URL+'/home/Follow-requests/reject', params: { headers: requestHeaders} },
        { method: 'DELETE', url: API_BASE_URL+'/messages/MohamedNano', params: { headers: requestHeaders} },


        

      ]);

    const req3 = {
        method: 'POST',
        url: 'http://mysirius.me:3000/home/retweet',
        params: {
          headers: { 'Authorization': 'Bearer ' +'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYyOGQ5NzUwNGUyNjA1NzJjZGEzYWFlMyIsImlhdCI6MTY1MzQ0NjU0MywiZXhwIjoxNjYyMDg2NTQzfQ.c4KeGfQmkpir4L-nmPJpMgANjmhFhtXuD7LRSyoG6MU'},
          body: { tweetID: '6267e4828e27c30923a68588',},
        },
      };
      const responses = http.batch([req3]);

    sleep(1)
};
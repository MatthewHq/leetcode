const fs = require('fs');
let rawdata = fs.readFileSync('data.json');
let festival = JSON.parse(rawdata);

let satArtists = []
for (const key in festival) {  
    let flag=false
    for (const innerKey in festival[key]) {  
        if (innerKey=="ref_date" &&festival[key][innerKey]=="2022-10-01"){
            flag=true 
        }
        if (flag && innerKey=="slug"){
            satArtists.push(festival[key][innerKey])
            // console.log(festival[key][innerKey])
        }
        // console.log(`${innerKey}: ${festival[key][innerKey]}`)
      }
  }

console.log(satArtists)


  
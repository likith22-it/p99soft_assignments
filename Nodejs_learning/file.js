const fs= require("fs");

setTimeout(() => {
    try {
        const data = fs.readFileSync("example.txt", "utf-8");
        console.log(data);
    } catch (err) {
        console.error("Error reading file:", err);
    }
}, 5000);


try{
    const data1= fs.readFile("example.txt","utf-8", (err, data) => {
        if (err) {
            console.error("Error reading file:", err);
        } else {
            console.log(data);
        }
    } );
}   catch(err){
    console.error("Error reading file:", err);
}
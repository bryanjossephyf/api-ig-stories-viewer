import  Express, { Application }  from "express";
import {exec} from "child_process"


const app: Application = Express()

//router

app.get("/api/:user", async (req,res)=> {
    const {user} = req.params
    exec(`python ig/igMain.py ${user}`, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error executing script: ${error.message}`);
            return res.status(500).send('Error executing script');
        }
        if (stderr) {
            console.error(`Script error: ${stderr}`);
            return res.status(500).send('Script error');
        }

        try {
            const userInfo = JSON.parse(stdout);
            res.status(200).json(userInfo);
        } catch (e:any) {
            console.error(`Parsing error: ${e.message}`);
            return res.status(500).send('Error parsing JSON');
        }
    })
}) 


//server

const PORT = process.env.PORT || 3000
app.listen(PORT,() => {
    console.log("Server is on")
})


const express =require('express');
const router =express.Router();
const User =require('../models/WEC');
const multer =require('multer');

var storage=multer.diskStorage({
    destination: function(req,file,cb){
        cb(null,"./uploads");
    },
    filename: function(req,file,cb){
        cb(null,file.filename + "_" + Date.now()+ "_"+ file.originalname)
    }
});
//iNSERT AN USER INTO DATABASE ROUTE
var upload = multer({
    storage: storage,
}).single('image');

router.post('/add',upload,(req,res)=>{
    const user=new User({
        sig: req.body.sig,
        Name: req.body.name,
        Type:req.body.type,
        date: req.body.date
    });
    user.save((err)=>{
        if(err){
            res.json({message: err.message,type: "danger"});
            return;

        }else{
            req.session.message = {
                type: "success",
                message: "Event added successfully"
            }
        };
        res.redirect("/")

    })
})

router.get("/",(req,res)=>{
    User.find().exec((err,users)=>{
        if(err){
            res.json({message : err.message})
        }else{
            res.render("index",{
                title: 'Home Page',
                users : users,

            })
        }
    })
});
router.get("/add",(req,res)=>{
    res.render("add_events",{title :"Add Events"});
    
    
})
router.get("/edit/:id",(req,res)=>{
    let id = req.params.id;
    User.findById(id,(err,user)=>{
        if(err){
            res.redirect('/');
        }else{
            res.render('edit_events',{
                title : "Edit User",
                user: user,
            })
        }

    })
})
//Update user route
router.post('/update/:id',upload,(req,res)=>{
    let id=req.params.id;
    User.findByIdAndUpdate(id,{
        sig: req.body.sig,
        Type: req.body.Type,
        Name: req.body.Name,
        date: req.body.date,

    },(err,result)=>{
        if(err){
            res.json({message: err.message,type:"danger"})
        }else{
            req.session.message = {
                type: 'success',
                message: 'User updated successfully!'
            };
            res.redirect("/");
        }
    })
});
// Delete User route
router.get('/delete/:id',(req,res)=>{
    let id = req.params.id;
    User.findByIdAndRemove(id,(err,result)=>{
        if(err){
            res.json({message: err.message})
        }else{
            req.session.message = {
                type : 'info',
                message : 'User Deleted Successfully!'
            };
            res.redirect('/');
        }
    })
})
module.exports = router;

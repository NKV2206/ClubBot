const mongoose =require('mongoose')
const userSchema =new mongoose.Schema({
    sig:{
        type:String,
        required:true,
    },
    Name: {
        type: String,
        required: true
    },
    Type: {
        type: String,
        required: true
    },
    date: { 
        type: String,
        required :true
    },
    created: {
        type :Date,
        required:true,
        default: Date.now

    }
});
module.exports = mongoose.model('WEC',userSchema);
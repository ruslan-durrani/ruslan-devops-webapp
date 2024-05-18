const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

const PORT = process.env.PORT || 5000;

// MongoDB connection
mongoose.connect('mongodb+srv://ruslandurrani907:ruslandurrani907@spotifycluster.djclun1.mongodb.net/', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.log(err));

// Schema
const UserSchema = new mongoose.Schema({
  name: String,
  email: String,
  phone: String,
  address: String
});

// Model
const User = mongoose.model('User', UserSchema);

app.get("/",(req,res)=>{
  res.json({"success":"App is running successfully"})
})
// Route to get user data
app.get('/api/user', async (req, res) => {
  try {
    const user = await User.findOne(); // Retrieve the first user found
    res.json(user);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));

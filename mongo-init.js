console.log("Running mongo-init.js")

// db = db.getSiblingDB(process.env.DB_NAME);
db = db.getSiblingDB('main');

// db.createUser(
//     {
//     user: process.env.DB_USER,
//     pwd: process.env.DB_PASS,
//     roles: [
//         { 
//             role: 'dbOwner', 
//             db: process.env.DB_NAME
//         }
//     ],
//     }
// );

db.createUser(
    {
    user: 'user',
    pwd: 'userpass',
    roles: [
        { 
            role: 'dbOwner', 
            db: 'main'
        }
    ],
    }
);

console.log("Completed mongo-init.js")

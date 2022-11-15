pragma solidity >=0.7.0 <0.9.0;

contract studentdata{
  struct student{
    int rollno;
    string fname;
    string lname;
    int marks;
  }

  address owner;
  int public count = 0;


  mapping(int => student) public std_records;

  modifier only_owner{
    require(owner == msg.sender);
    _;
  }

  constructor() public{
    owner = msg.sender;
  }

  function add_new_records(int rno, string memory f_name, string memory l_name, int mark) public only_owner{
    count+=1;
    std_records[count] = student(rno, f_name, l_name, mark);
  }

  function bonus_marks(int bonus) public only_owner{
    std_records[count].marks = std_records[count].marks + bonus;
  }

  fallback() external payable{}
  
}
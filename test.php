<?php
/* connect to server */
$hostname = '{imap.gmail.com:993/imap/ssl}INBOX';
$username = 'refreshstatusc9@gmail.com';
$password = 'd2z4BJxeSUVv';

/* try to connect */
$inbox = imap_open($hostname,$username,$password) or die('Cannot connect to Tiriyo: ' . imap_last_error());
//echo $inbox;
/* grab emails */
$emails = imap_search($inbox,'ALL');

/* if emails are returned, cycle through each... */
if($emails) {

  /* begin output var */
  $output = '';

  /* put the newest emails on top */
  rsort($emails);

  /* for every email... */
  foreach($emails as $email_number) {
    //$email_number=$emails[0];
//print_r($emails);
    /* get information specific to this email */
    $overview = imap_fetch_overview($inbox,$email_number,0);
    $message = quoted_printable_decode(imap_fetchbody($inbox,$email_number,2));

    /* output the email header information */
    $output.= '<div class="toggler '.($overview[0]->seen ? 'read' : 'unread').'">';
    $output.= '<span class="subject">'.$overview[0]->subject.'</span> ';
    $output.= '<span class="from">'.$overview[0]->from.'</span>';
    $output.= '<span class="date">on '.$overview[0]->date.'</span>';
    $output.= '</div>';

    /* output the email body */
    $output.= '<div class="body">'.$message.'</div>';
  }

  echo $output;
}

/* close the connection */
imap_close($inbox);
?>
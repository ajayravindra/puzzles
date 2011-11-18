#include <stdio.h>
#include <string.h>

#define MAXLEN 255

void next_seq( char * seq ) {

  char next_seq[MAXLEN];
  int freq, i, len;

  if ( !seq || strlen(seq) == 0 ) {
    printf( "(ERROR) %s[%d]: seq is NULL\n", __func__, __LINE__ );
    return;
  }

  if ( strlen(seq) == 1 ) {
    snprintf( seq, MAXLEN, "1%c", seq[0]);
    return;
  }

  bzero( next_seq, MAXLEN);
  len = 0;

  for ( i = 1, freq = 1; i < strlen( seq ); i++ ) {
    //printf( "DBG: i=%d; seq[%d]=%c; len=%d\n", i, i, seq[i], len );
    if ( seq[i] == seq[i-1] ) {
      freq ++;
    } else {
      //printf("%d%c", freq, seq[i-1]);
      len += snprintf( next_seq + len, MAXLEN - len, "%d%c", freq, seq[i-1] );
      freq = 1;
    }
  }
  
  //printf("%d%c\n", freq, seq[i-1]);
  snprintf( next_seq + len, MAXLEN - len, "%d%c", freq, seq[i-1] );
  strncpy( seq, next_seq, MAXLEN );

}

int main( void ) {

  int series_len, i;
  char seq[MAXLEN];

  printf( "enter sequence length: " );
  scanf( "%d", &series_len );

  if ( series_len <= 0 || series_len > 10 ) {
    printf( "length should be in [1, 10]\n" );
    return( 0 );
  }

  printf( "%2d: 1\n" , 1);

  if ( series_len == 1 ) {
    return( 0 );
  }

  bzero( seq, MAXLEN );
  strcpy( seq, "1" );

  for ( i = 1; i < series_len; i ++ ) {
    next_seq( seq );
    printf ("%2d: %s\n", i+1, seq);
  }

  return( 0 );
}


#include <stdio.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <string.h>


#define PORT 8080
#define DATA_QUANTITY 1

/*
* Brief: Recieves data through a pre configured socket
*
* Parameters:
* int socket - A pre configured socket
* int* buffer - pointer to the content vector that will keep the 3 recieved integers
*/
void recieve_data(int socket, int* buffer) {
  read(socket, buffer, 3*sizeof(int));
}

int main() {
    // Socket configuration
    int socket_connection = 0;
    socket_connection = socket(AF_INET, SOCK_STREAM, 0);

    struct sockaddr_in server_address;
    memset(&server_address, '0', sizeof(server_address));

    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(PORT);

    inet_pton(AF_INET, "127.0.0.1", &server_address.sin_addr);

    connect(socket_connection, (struct sockaddr*)&server_address, sizeof(server_address));

    // Data recieving
    int content[3] = {0};

    int x = 0;

    for(x = 0; x < DATA_QUANTITY; x++) {
      recieve_data(socket_connection, content);
      printf("X:%d Y:%d Z:%d\n", content[0], content[1], content[2]);
    }

    return 0;
}

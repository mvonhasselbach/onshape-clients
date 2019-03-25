/**
 * Onshape REST API
 * The Onshape REST API consumed by all clients.
 *
 * OpenAPI spec version: 1.93
 * Contact: api-support@onshape.zendesk.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { BTTeamSummaryInfo } from './bTTeamSummaryInfo';
import { BTUserSummaryInfo } from './bTUserSummaryInfo';

export class BTIdentityInfo {
    'team'?: BTTeamSummaryInfo;
    'identityType'?: number;
    'user'?: BTUserSummaryInfo;
    'name'?: string;
    'id'?: string;
    'href'?: string;
    'viewRef'?: string;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "team",
            "baseName": "team",
            "type": "BTTeamSummaryInfo"
        },
        {
            "name": "identityType",
            "baseName": "identityType",
            "type": "number"
        },
        {
            "name": "user",
            "baseName": "user",
            "type": "BTUserSummaryInfo"
        },
        {
            "name": "name",
            "baseName": "name",
            "type": "string"
        },
        {
            "name": "id",
            "baseName": "id",
            "type": "string"
        },
        {
            "name": "href",
            "baseName": "href",
            "type": "string"
        },
        {
            "name": "viewRef",
            "baseName": "viewRef",
            "type": "string"
        }    ];

    static getAttributeTypeMap() {
        return BTIdentityInfo.attributeTypeMap;
    }
}

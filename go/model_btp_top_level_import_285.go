/*
 * Onshape REST API
 *
 * The Onshape REST API consumed by all clients.
 *
 * API version: 1.111
 * Contact: api-support@onshape.zendesk.com
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi
// BtpTopLevelImport285 struct for BtpTopLevelImport285
type BtpTopLevelImport285 struct {
	Atomic bool `json:"atomic,omitempty"`
	BtType string `json:"btType,omitempty"`
	DocumentationType string `json:"documentationType,omitempty"`
	EndSourceLocation int32 `json:"endSourceLocation,omitempty"`
	NodeId string `json:"nodeId,omitempty"`
	ShortDescriptor string `json:"shortDescriptor,omitempty"`
	SpaceAfter BtpSpace10 `json:"spaceAfter,omitempty"`
	SpaceBefore BtpSpace10 `json:"spaceBefore,omitempty"`
	SpaceDefault bool `json:"spaceDefault,omitempty"`
	StartSourceLocation int32 `json:"startSourceLocation,omitempty"`
	Deprecated bool `json:"deprecated,omitempty"`
	SymbolName BtpIdentifier8 `json:"symbolName,omitempty"`
	ArgumentsToDocument []BtpArgumentDeclaration232 `json:"argumentsToDocument,omitempty"`
	DeprecatedExplanation string `json:"deprecatedExplanation,omitempty"`
	ForExport bool `json:"forExport,omitempty"`
	SpaceAfterExport BtpSpace10 `json:"spaceAfterExport,omitempty"`
	Annotation BtpAnnotation231 `json:"annotation,omitempty"`
	ImportMicroversion string `json:"importMicroversion,omitempty"`
	NamespaceString string `json:"namespaceString,omitempty"`
	CombinedNamespacePathAndVersion string `json:"combinedNamespacePathAndVersion,omitempty"`
	ModuleId BtpModuleId235 `json:"moduleId,omitempty"`
	SpaceBeforeImport BtpSpace10 `json:"spaceBeforeImport,omitempty"`
	Namespace []BtpIdentifier8 `json:"namespace,omitempty"`
}